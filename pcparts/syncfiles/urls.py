from django.urls import path
from . import views

urlpatterns = [
    path('syncfiles/', views.members, name='syncfiles'),
]

