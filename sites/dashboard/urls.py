from django.contrib import admin
from django.urls import path
from dashboard import views
urlpatterns = [
    path('student_list/', views.student_list),
    path('student_add/', views.student_add),
    path('student_edit/<int:sid>', views.student_edit),
    path('course_list/', views.course_list),
    path('course_add/', views.course_add),
    path('course_edit/<int:cid>', views.course_edit)
]