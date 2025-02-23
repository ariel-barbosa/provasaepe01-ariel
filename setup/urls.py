from django.urls import path
from crud.views import listar_tarefas, adicionar_tarefa, editar_tarefa

urlpatterns = [
    path('', listar_tarefas, name='listar_tarefas'),
    path('adicionar/', adicionar_tarefa, name='adicionar_tarefa'),
    path('editar/<int:id_tarefa>/', editar_tarefa, name='editar_tarefa'),
]
