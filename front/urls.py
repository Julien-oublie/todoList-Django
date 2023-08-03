from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('getTodo/',views.getTodo, name='getTodo'),
    path('newTodo/',views.newTodo,name='newTodo'),
    path('modify/',views.modifiyTodo, name="modifyTodo"),
    path('deleteTodo/',views.deleteTodo, name='deleteTodo')
    
]