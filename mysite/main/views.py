from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    print(response.POST)
 
    if response.method == "POST":
        if response.user.username == ls.user.username:
            print("sameuser")
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
        
                    item.save()
        
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
        
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

            elif response.POST.get("delItem"):
                itemId = int(response.POST.get("delItem").split(",")[0])
                print(itemId)
                item = [item for item in ls.item_set.all() if itemId == item.id][0]
                item.delete()

                return HttpResponseRedirect("/%i" %id)
        else:
            print("notsame")
 
 
    return render(response, "main/list.html", {"ls":ls})

def glossary(response):
    ToDos = response.user.todolist.all()
    if response.method == "POST":
        if response.POST.get("delItem"):
                lsId = int(response.POST.get("delItem").split(",")[0])
                print(lsId)
                todo = [todo for todo in ToDos if lsId == todo.id][0]
                todo.delete()

                return HttpResponseRedirect("/glossary")

 
    return render(response, "main/glossary.html", {})

def glossaryall(response):
    ToDos = ToDoList.objects.all()
    return render(response, "main/glossaryall.html", {"ToDos":ToDos})

def home(response):
    return render(response,"main/home.html",{})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response,"main/create.html",{"form":form})

