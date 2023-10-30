from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskUpdateForm
from django.views.generic import  ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

class TaskListView(ListView):
    model=Task
    template_name='add_task.html'
    context_object_name='taskdetails'


class TaskDetailView(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='task'

class TaskUpdateView(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})


class TaskDeleteView(DeleteView):
    model=Task
    template_name='update.html'
    context_object_name='task'
    success_url=reverse_lazy('adddv')

    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

def add_task(request):
    taskdetails = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority,date=date)
        task.save()
    return render(request, 'add_task.html', {'taskdetails': taskdetails})



def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskUpdateForm(request.POST or None , instance=task)
    if form.is_valid():
        form.save()
        return redirect('add')  
    return render(request, 'update_task.html', {'form': form, 'task': task})


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('add')  
