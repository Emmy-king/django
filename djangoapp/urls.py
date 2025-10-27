from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('database/', views.database, name='database'),
    path('update/<int:id>', views.update, name='update'),
]