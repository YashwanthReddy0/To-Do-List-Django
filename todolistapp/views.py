from django.shortcuts import render, redirect
from todolistapp.models import DeletedTask, Todolist

# Create your views here.
def todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        
        Todolist.objects.create(task=task, description=description)
               
    return render(request, 'main.html')

def display(request):
    data = Todolist.objects.all()
    context = {
        'data': data
    }
    return render(request, 'display.html', context)



def details(request, pk):
    data = Todolist.objects.get(id=pk)
    if request.method == 'POST':
        DeletedTask.objects.create(task=data.task, description=data.description)
        data.delete()
        return redirect('todo')
    context = {
        'data': data
    }
    return render(request, 'details.html', context)


def edit(request, pk):
    data = Todolist.objects.get(id=pk)
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        
        data.task = task
        data.description = description
        data.save()
        
        return redirect('display')
    context = {
        'data': data
    }
    return render(request, 'edit.html', context)

def history(request):
    deleted_tasks = DeletedTask.objects.all()
    if request.method == 'POST':
        task_id = request.POST.get('delete')
        if task_id:
            task = DeletedTask.objects.get(id=task_id)
            task.delete()
        return redirect('history')

    context = {
        'data': deleted_tasks
    }
    return render(request, 'history.html', context)




