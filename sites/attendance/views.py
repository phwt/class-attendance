from django.http import HttpResponse
from django.shortcuts import render


def subject(request):
    return HttpResponse('Show today subject')

def course(request, id):
    return HttpResponse('วิชานี้สอนอะไร, มีจำนวนนักเรียนกี่คน, มีคนมาเรียน และขาดกี่คน')

def qrcode(request):
    return HttpResponse('QR Code')