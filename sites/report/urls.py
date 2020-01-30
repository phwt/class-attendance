from django.contrib import admin
from django.urls import path
from report import views
urlpatterns = [
    path('dashboard/', views.dashboard),
    path('find/<int:sid>', views.find)
]