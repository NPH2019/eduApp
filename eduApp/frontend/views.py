from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


@require_http_methods(["GET"])
def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')


@require_http_methods(["GET"])
def cls(request):
    if request.method == 'GET':
        return render(request, 'class.html')


@require_http_methods(["GET"])
def learning(request):
    if request.method == 'GET':
        return render(request, 'online-learning.html')


@require_http_methods(["GET"])
def lesson(request):
    if request.method == 'GET':
        return render(request, 'lesson.html')


@require_http_methods(["GET"])
def login_client(request):
    if request.method == 'GET':
        return render(request, 'login-client.html')


@require_http_methods(["GET"])
def login_instructions(request):
    if request.method == 'GET':
        return render(request, 'login-instructions.html')


@require_http_methods(["GET"])
def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')


@require_http_methods(["GET"])
def search(request):
    if request.method == 'GET':
        return render(request, 'search.html')
