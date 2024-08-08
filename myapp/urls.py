from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home),
    path('lista_presidentes', views.list_presidentes),
    path('lista_presidentes/<int:id>', views.detail_presidentes),
]