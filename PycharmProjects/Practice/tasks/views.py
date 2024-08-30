from django.db.models import Q
from django.shortcuts import render, redirect

from tasks.forms import SearchForm, TaskForm
from tasks.models import Task


def base_view(request):
    if request.method == 'GET':
        return render(request, 'base.html')


def task_list_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        category = request.GET.get('category')
        searchform = SearchForm(request.GET)
        tasks = Task.objects.all()
        if search:
            tasks = tasks.filter(Q(title__icontains=search))
        if category:
            tasks = tasks.filter(category__id__in=category)
        context = {'tasks': tasks, 'search_form': searchform}
        return render(request, 'task_list.html', context=context)


def task_detail_view(request, task_id):
    if request.method == 'GET':
        task = Task.objects.get(id=task_id)
        return render(request, 'task_detail.html', context={'task': task})


def task_create_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', context={'form': form})
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if not form.is_valid():
            return render(request, 'task_create.html', context={'form': form})
        form.save()
        return redirect('/tasks/')
