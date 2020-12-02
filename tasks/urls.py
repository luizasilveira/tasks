
from django.urls import path
from . import views
# from .views import TaskCreate, TaskList, TaskDelete, TaskUpdate
from .views import get_tasks

urlpatterns = [
    path('get', views.get_tasks),
    path('post', views.post_task),
    path('delete', views.delete_tasks)
]