from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('atualizar/<int:id_tarefa>/', views.atualizar_tarefa, name='atualizar_tarefa'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'), # Adicionado
]