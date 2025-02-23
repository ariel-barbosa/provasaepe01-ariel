from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa, Usuario
from .forms import UsuarioForm, TarefaForm

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    formulario = TarefaForm()

    return render(request, 'crud/listar_tarefas.html', {'tarefas': tarefas, 'formulario': formulario})

def editar_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')  # Redireciona para a página principal
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'crud/editar_tarefa.html', {'form': form, 'tarefa': tarefa})


def adicionar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    return redirect('listar_tarefas')  # Redireciona de volta


def editar_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'crud/editar_tarefa.html', {'form': form})
