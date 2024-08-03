from django.urls import path
from . import views

urlpatterns = [
    path('hdds/', views.hdds, name='hdds'),
    path('hdds/add/', views.add, name='add'),
    path('hdds/add/addrecord/', views.addrecord, name='addrecord'),
    path('hdds/delete/<int:id>', views.delete, name='delete'),
    path('hdds/update/<int:id>', views.update, name='update'),
    path('hdds/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
