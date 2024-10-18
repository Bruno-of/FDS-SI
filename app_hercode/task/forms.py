from django import forms
from .models import VideoAula

class VideoAulaF(forms.ModelForm):
    class Meta:
        model = VideoAula
        fields = ['titulo', 'descricao', 'arquivo_video']
