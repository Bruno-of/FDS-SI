from django.db import models

# Create your models here.


class Quiz(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.CharField(max_length=300)

    def __str__(self):
        return self.texto


class Opcao(models.Model):
    pergunta = models.ForeignKey(
        Pergunta, on_delete=models.CASCADE, related_name='opcoes')
    texto = models.CharField(max_length=200)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto


class VideoAula(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    arquivo_video = models.FileField(upload_to='videos/')
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
