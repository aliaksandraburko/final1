from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib import messages

## import todo form and models
from django.urls import reverse

from .forms import TodoForm
from .models import Todo


###############################################

def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",

    }
    return render(request, 'todo/index.html', page)


### function to remove item, it recive todo item id from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed!!!")
    return redirect('todo')


def check(request, item_id):
    check = Todo.objects.get(id=item_id)
    check.delete()
    messages.info(request, 'you do it! Well!!!')
    return redirect('todo')


def completeTodo(request, item_id):
    todo = Todo.objects.get(pk=item_id)
    todo.complete = True
    todo.save()
    return redirect('todo')



def edit(request, item_id):
    if request.method == 'GET':
        todo = Todo.objects.filter(id=item_id).first()
        return render(request, 'index.html')
    elif request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Todo.objects.filter(id=item_id).update(**data)
            messages.add_message(
                request,
                messages.INFO,
                f'todo " {item_id}" updated successfully',
            )
            return redirect('todo')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')