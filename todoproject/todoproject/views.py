from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo_form.html', {'form': form, 'title': 'Add To-Do'})

def todo_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo_view.html', {'todo': todo})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo_form.html', {'form': form, 'title': 'Edit To-Do'})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')
