# FDS-SI
>**Repositório destinado ao projeto da cadeira de Fundamentos de desenvolvimento de software do 2° período de sistemas de informação no Cesar School.**

## Nosso projeto

Estamos desenvolvendo uma plataforma chamada HerCode, com ela, nós alunos buscamos aprofundar nosso conhecimento em Python e Django, visto que HerCode será uma aplicação web desenvolvida utilizando, principalmente, estas linguagens de programação. A HerCode será uma plataforma educacional voltada para o ensino de programação e tecnologia, especialmente para mulheres, uma vez que nesse projeto, focamos nas ODS 4 e 5; Educação de Qualidade e Igualdade de Gênero. A aplicação web que iremos criar deverá disponibilizar cursos, videoaulas e atividades para melhor desenvolver a compreensão do aluno sobre sua matéria desejada.

---

## Ferramentas utilizadas
<details>
  <summary>Clique para expandir</summary>

- **Google drive**: O google drive foi utilizado como repositório para nossos documentos.
- **Google docs**: O google docs foi utilizado como editor de textos colaborativo.
- **Jira**: Utilizamos o jira para organizar as tarefas, datas de entregas e o cronograma do projeto.
- **Whatsapp**: O whatsapp foi usado para comunicação a partir de mensagens.
- **Discord**: Reuniões online foram realizadas pelo discord.
- **Figma**: Utilizamos o figma para criação do canvas no início do nosso projeto.
- **HTML**: Utilizamos HTML para estruturar as páginas da nossa aplicação web.
- **CSS**: Utilizamos CSS para estilizar as páginas da aplicação.
- **Python**: Python foi utilizado como linguagem de backend.
- **Django**: Django foi o framework usado.
- **SQLite**: Banco de dados utilizado no projeto.
- **Github**: Utilizamos o GitHub para versionamento.
- **Git**: Controle de versão com Git.
- **VS Code**: Editor de código utilizado.
- **Click Up**: Usado para o board contendo backlog, historias e as sprints.

</details>

---

## Nossa Equipe

- Paulo Henrique Egito
- Maria Luisa Albuquerque Bandeira de Carvalho
- Fernanda Ramalho Bezerra
- Bruno Oliveira de Macêdo Filho
- Matheus Miranda Escorel
- Pedro Augusto Simões Calazans Dutra
- Jorge Augusto Lacerda Vasconcelos
- Luis Filipe Brigido Teles


---

## Entrega 01
<details>
  <summary>Clique para expandir</summary>
  
## Board do Jira
![image](https://github.com/user-attachments/assets/5f6359a9-ef89-4441-9eee-473acbc286f1)

## Backlog do Jira
![image](https://github.com/user-attachments/assets/647dd12f-0e14-4d49-8eaf-612d0398fc24)
![image](https://github.com/user-attachments/assets/c264e364-ad3b-4f64-ae39-6c014e940bb7)

## ScreenCast apresentando o protótipo
https://drive.google.com/file/d/1ldtQyUqsxz38KBShmw-UVgkj1_8hVdXX/view

## Protótipos Lo-fi no Figma
https://www.figma.com/board/tLBpTiOs7D14jfbMT4Gqdx/HerCode-%5BFDS%5D?node-id=0-1&t=jxbuFcZCubKfOgzH-1
</details>

---

## Entrega 02
<details>
  <summary>Clique para expandir</summary>
  
  ## Board do ClickUp
  ![image](https://github.com/user-attachments/assets/83661190-1757-421b-a5ab-6bff87dcca1d)

  ## Diagrama de atividades
  https://www.figma.com/board/tLBpTiOs7D14jfbMT4Gqdx/HerCode-%5BFDS%5D?node-id=0-1&t=vt7ZICxzgjbOG55g-1

  ## ScreenCast apresentando a aplicação
  https://github.com/user-attachments/assets/b84ddeef-52fc-462b-9e94-1dd31d3794ed


  ## Programação em pares
  A experiência de programação em pares no nosso grupo de 9 pessoas foi um pouco diferente, pois adotamos uma abordagem baseada em trios em vez de duplas tradicionais. Isso nos permitiu distribuir as responsabilidades de maneira equilibrada,    garantindo que cada trio fosse responsável por uma parte específica do projeto.

Durante o processo, agendávamos chamadas em trio para programarmos juntos, focando nas features ou histórias nas suas respectivas branches. Além disso, também nos reuníamos como grupo inteiro para alinhar o progresso e garantir que todos estivessem na mesma página. Um aspecto importante foi a criação de pull requests (PRs) para aprovar mudanças mais significativas, o que trouxe uma camada de revisão entre os membros, garantindo a qualidade do código.

Por outro lado, ao trabalharmos em duplas, focamos mais nos comandos do Git, como criar branches, fazer commits e resolver conflitos de merge. Um membro da dupla executava as tarefas práticas, enquanto o outro observava e identificava possíveis erros ou melhorias, o que nos ajudou a evitar problemas mais sérios e a melhorar nosso fluxo de trabalho em equipe.
</details>

---

## Como execultar o projeto 
> **Nota:** Este guia descreve como clonar e configurar o projeto HerCode em sua máquina.

### Pré-requisitos

- **Python 3.x**: Certifique-se de ter o Python 3.x instalado.
- **Django admin**: Certifique-se de ter o Django instalado.
- **Git**: Necessário para clonar o repositório.

### Passo a Passo
No terminal do VSCode faça: 

```bash
# Passo 1: Clonar o Repositório
git clone https://github.com/Bruno-of/FDS-SI.git
#Isso criará uma cópia do repositório na pasta atual. Navegue até o diretório do projeto:

# Passo 2: Acesse a pasta do projeto:
cd app_hercode

# Passo 3: Executar o Servidor Local
#Inicie o servidor local do Django com o comando:
python manage.py runserver
# O servidor estará acessível em http://127.0.0.1:8000/. Abra este endereço em seu navegador para acessar o HerCode localmente.

# Passo 4: Acessar o Projeto
#Para acessar o sistema e explorar suas funcionalidades:
URL Principal: http://127.0.0.1:8000/
Admin (caso tenha criado um superusuário): http://127.0.0.1:8000/admin


