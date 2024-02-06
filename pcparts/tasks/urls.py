from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/addtask/', views.addtask, name='addtask'),
    path('tasks/addtask/addrecord/', views.addrecord, name='addrecord'),
    path('tasks/delete/<int:id>', views.delete, name='delete'),
    path('tasks/update/<int:id>', views.update, name='updatetask'),
    path('tasks/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
