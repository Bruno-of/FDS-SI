from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Quiz, Opcao
# Home do Projeto


def home(request):
    return render(request, 'home.html')

# Cadastro de usuário (signup)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            email = request.POST.get('email')
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            # Verifica se já existe um usuário com o mesmo email
            if User.objects.filter(email=email).exists():
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Este email já está em uso'
                })

            # Verifica se já existe um usuário com o mesmo nome de usuário (username)
            if User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Este nome de usuário já está em uso'
                })

            try:
                # Cria o usuário com nome, sobrenome, username e email
                user = User.objects.create_user(
                    username=username,
                    password=request.POST['password1'],
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()

                login(request, user)
                return redirect('home')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Erro ao criar usuário'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'As senhas são diferentes'
        })

# Login de usuário (signin)


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuário ou senha está incorreto'
            })
        else:
            login(request, user)
            return redirect('tasks')

# Logout de usuário (sair)


@login_required
def sair(request):
    logout(request)
    return redirect('home')

# Página de tarefas (tasks)


@login_required
def tasks(request):
    return render(request, 'tasks.html')


# Página de quizzes
def quizzes(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizz.html', {'quizzes': quizzes})


def quiz_perguntas(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        acertos = 0
        total = quiz.perguntas.count()
        resultados = []

        for pergunta in quiz.perguntas.all():
            resposta_id = request.POST.get(f'pergunta_{pergunta.id}')
            if resposta_id:
                opcao = Opcao.objects.get(id=resposta_id)
                if opcao.correta:
                    acertos += 1
                    resultados.append({
                        'pergunta': pergunta.texto,
                        'correta': True,
                        'resposta_usuario': opcao.texto
                    })
                else:
                    opcao_correta = pergunta.opcoes.get(correta=True)
                    resultados.append({
                        'pergunta': pergunta.texto,
                        'correta': False,
                        'resposta_usuario': opcao.texto,
                        'resposta_correta': opcao_correta.texto
                    })

        # Passar resultados, acertos e total para a sessão
        request.session['resultados'] = resultados
        request.session['acertos'] = acertos
        request.session['total'] = total

        return redirect('resultados', quiz_id=quiz_id)

    return render(request, 'quizz_perguntas.html', {'quiz': quiz})


def quiz_resultados(request, quiz_id):
    # Recuperar os dados da sessão
    resultados = request.session.get('resultados', [])
    acertos = request.session.get('acertos', 0)
    total = request.session.get('total', 0)

    context = {
        'resultados': resultados,
        'acertos': acertos,
        'total': total
    }
    return render(request, 'resultados.html', context)
