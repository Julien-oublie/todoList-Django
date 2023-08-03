from cgitb import reset
from operator import imod
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from front.models import TodoList
from django.utils import timezone
import requests
import json

# Create your views here.
# request -> response "le controlleur pour symfo"



def index(request):
    ## reçoios les donées de l'api
    
    return render(request,'hello.html',{}) #dans les crochets met des clées valeur like this man 'prenom':'julien' #


def getTodo(request):
    ## reçoios les donées de l'api
    
    todolist = TodoList.objects.all()
    
    return JsonResponse({'datas': list(todolist.values())}) 


def newTodo(request):
    todoList = TodoList(todo=request.POST.get('todo'), pubDate=timezone.now())
    todoList.save()

    return JsonResponse({'message':"c'est bien ajouté poto"})

def modifiyTodo(request):

    status = False if request.POST.get('status') == 'false' else True
    todoList = TodoList.objects.get(pk=request.POST.get('id'))
    todoList.status = status
    todoList.todo = request.POST.get('todo')
    todoList.save()

    return JsonResponse({'message':"c'est bien modifié"})

def deleteTodo(request):
    # Récupérer l'article avec l'ID 2
    todoList = TodoList.objects.get(pk=request.POST.get('id'))

    # Supprimer l'article
    todoList.delete()

    return JsonResponse({'message':"c'est bien delete"})

