from django.db import models

class Tarefa(models.Model):
    PRIORIDADE_OPCOES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    STATUS_OPCOES = [
        ('a_fazer', 'A Fazer'),
        ('fazendo', 'Fazendo'),
        ('pronto', 'Pronto'),
    ]

    id_usuario = models.IntegerField()
    descricao = models.TextField()
    nome_setor = models.CharField(max_length=100)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_OPCOES)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_OPCOES, default='a_fazer')

    def __str__(self):
        return self.descricao
    
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

