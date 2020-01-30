from django.contrib import admin
from django.urls import path
from attendance import views
urlpatterns = [
    path('subject/', views.subject),
    path('course/<int:id>', views.course),
    path('qrcode/', views.qrcode)
]
