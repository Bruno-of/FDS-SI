from django.contrib import admin
from .models import Quiz, Pergunta, Opcao
# Register your models here.
admin.site.register(Quiz)


class OpcaoInline(admin.TabularInline):
    model = Opcao


class PerguntaAdmin(admin.ModelAdmin):
    inlines = [OpcaoInline]


admin.site.register(Pergunta, PerguntaAdmin)
