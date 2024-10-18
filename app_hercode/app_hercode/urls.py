"""
URL configuration for app_fact project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('perfil/', views.perfil, name='perfil'),
    path('sair/', views.sair, name='sair'),
    path('quizz/', views.quizzes, name='quizz'),
    path('<int:quiz_id>/', views.quiz_perguntas, name='quiz_perguntas'),
    path('resultados/<int:quiz_id>/', views.quiz_resultados, name='resultados'),
    path('video_aulas/', views.lista_videoaulas, name='lista_videoaulas'),
    path('adicionar-videoaula/', views.adicionar_videoaula, name='adicionar_videoaula'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
