from django.shortcuts import render
from django.views.decorators.http import require_http_methods


# Create your views here.
# Class
@require_http_methods(["GET"])
def sclass(request):
    if request.method == 'GET':
        return render(request, 'class/index.html')


# Lesson
@require_http_methods(["GET"])
def lesson(request):
    if request.method == 'GET':
        return render(request, 'lesson/index.html')


# Subject
@require_http_methods(["GET"])
def subject(request):
    if request.method == 'GET':
        return render(request, 'subject/index.html')


# Programme
@require_http_methods(["GET"])
def programme(request):
    if request.method == 'GET':
        return render(request, 'programme/index.html')
