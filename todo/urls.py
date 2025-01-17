"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

# 本地的
from . import views

urlpatterns = [
    path("", views.todo, name="todo"),
    path("todo/<int:id>", views.view_todo, name="view_todo"),
    path("create-todo/", views.create_todo, name="create_todo"),
    path("completed-todo/", views.completed_todo, name="completed_todo"),
    path("delete-todo/<int:id>", views.delete_todo, name="delete_todo"),
    path(
        "completed_todo'/<int:id>",
        views.completed_todo_byid,
        name="completed_todo_byid",
    ),
    path(
        "uncompleted_todo'/<int:id>",
        views.uncompleted_todo_byid,
        name="uncompleted_todo",
    ),
]
