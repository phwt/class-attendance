from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse('Dashboard')

def find(request, sid):
    return HttpResponse(f'Finding: {sid}')