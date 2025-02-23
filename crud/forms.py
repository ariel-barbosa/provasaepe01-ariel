from django import forms
from .models import Tarefa, Usuario

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['descricao', 'nome_setor', 'prioridade', 'status']
        widgets = {
            'prioridade': forms.Select(choices=[
                ('baixa', 'Baixa'),
                ('media', 'Média'),
                ('alta', 'Alta'),
            ]),
            'status': forms.Select(choices=[
                ('a_fazer', 'A Fazer'),
                ('fazendo', 'Fazendo'),
                ('pronto', 'Pronto'),
            ]),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email']
