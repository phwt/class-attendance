from django.shortcuts import render
from django.http import HttpResponse

def student_list(request):
    return HttpResponse('student_list')

def student_add(request):
    return HttpResponse('student_add')

def student_edit(request, sid):
    return HttpResponse(f'student_edit: {sid}')

def course_list(request):
    return HttpResponse('course_list')

def course_add(request):
    return HttpResponse('course_add')

def course_edit(request, cid):
    return HttpResponse(f'course_edit: {cid}')

