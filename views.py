from django.shortcuts import render , get_object_or_404 , redirect

#return http response 
from django.http import HttpResponse
#IMPORT MODELS
from .models import Task , Category 
from .forms import TaskForm , CategoryForm

#  Create your views here.

#   Function base view 


def index(request):
    #SELECT * from Task ;
    tasks = Task.objects.all().order_by('due_date')
    # tasks = Task.objects.filter(status ='PENDING' )
    categories = Category.objects.all()

    context = { 'tasks':tasks ,
                'categories' :categories
              }
    # return HttpResponse(tasks)
    return render(request , 'main/index.html',context)


def detailed_task(request ,id):
    
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task , id=id)

    context = {
        'task':task
    }
    return render(request , 'main/detailed.html' , context)


def todo_by_status(request , st):
    todos = Task.objects.filter(status = st)
    context = {
        'todos' :todos
    }
    return render(request , 'main/todosstatus.html' , context)




def Todo_list_Category(request  , id):
    todos = Task.objects.filter(category=id)
    categories = Category.objects.all()

    context = {
        "tasks" : todos ,
        'categories' :categories

    }
    return render(request , 'main/index.html',context)


#create task 
def Createtodo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid() :
            form.save() #--> save the record in database            
            return redirect('home')
    else:  
        form = TaskForm()
    return render(request , 'main/create_todo.html' ,{'form' :form} )



def createCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid() :
            form.save() #--> save the record in database            
            return redirect('home')
    else:  
        form = CategoryForm()
    return render(request , 'main/createCategorys.html' ,{'form':form})



def update_task(request , id ):
    task = get_object_or_404(Task , id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid() :
            form.save() #--> save the record in database            
            return redirect('home')
    else:  
        form = TaskForm(instance=task)
    return render(request, 'main/updatetask.html' , {'form':form})

def delete_task(request , id):
    task = get_object_or_404(Task , id=id)
    task.delete()
    return redirect('home')



