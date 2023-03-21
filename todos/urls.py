from django.urls import path
from .views import ListTodo, DetailTodo
urlpatterns = [
path("todo_list/<int:pk>/", DetailTodo.as_view(), name="todo_detail"),
path("todo_list/", ListTodo.as_view(), name="todo_list"),
]
