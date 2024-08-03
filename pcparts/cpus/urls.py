from django.urls import path
from . import views

urlpatterns = [
    path('cpus/', views.cpus, name='cpus'),
    path('cpus/add/', views.add, name='add'),
    path('cpus/add/addrecord/', views.addrecord, name='addrecord'),
    path('cpus/delete/<int:id>', views.delete, name='delete'),
    path('cpus/update/<int:id>', views.update, name='update'),
    path('cpus/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
