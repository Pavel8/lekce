from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('temp/', views.members2, name='members2'),
]