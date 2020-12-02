
from django.urls import path
from . import views
# from .views import TaskCreate, TaskList, TaskDelete, TaskUpdate
from .views import getTasks

urlpatterns = [
    path('get', views.getTasks),
    path('post', views.createTask),
    path('delete', views.deleteTasks)
]