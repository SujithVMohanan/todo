from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from .models import Tasks
from .forms import TodoForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

class TaskListView(ListView):
    model = Tasks
    template_name = 'home.html'
    context_object_name = 'tasks'


class TaskDetailsView(DetailView):
    model = Tasks
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Tasks
    template_name = 'update.html'
    context_object_name = 'task'

    fields = ['task', 'priority', 'date']

    def get_success_url(self):
        return reverse_lazy('todoapp:details', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')


def home(request):
    tasks = Tasks.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')

        task = Tasks(task=name, priority=priority, date=date)
        task.save()

    return render(request, 'home.html', {'tasks': tasks, })


def delete(request, t_id):
    task = Tasks.objects.get(id=t_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', )


def update(request, uid):
    task = Tasks.objects.get(id=uid)
    f = TodoForm(request.POST or None, instance=task)

    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'f': f, 't': task})
