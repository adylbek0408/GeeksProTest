from django.urls import path
from .views import TaskViewSets

urlpatterns = [
    path('task/', TaskViewSets.as_view({'get': 'list'}),
         name='task_list'),
    path('task/<int:pk>/',
         TaskViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='task_detail'),
]


# 
