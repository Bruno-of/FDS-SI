from django import forms
from django.contrib.auth.models import User
from .models import VideoAula


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class VideoAulaF(forms.ModelForm):
    class Meta:
        model = VideoAula
        fields = ['titulo', 'descricao', 'arquivo_video']
