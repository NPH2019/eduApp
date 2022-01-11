from django.shortcuts import render
from eduApp.backend.study_program.models import Program, Class
from django.views.decorators.http import require_http_methods
from eduApp.backend.about_us.models import About


@require_http_methods(["GET"])
def index(request):
    if request.method == 'GET':
        obj = Program.objects.filter(program_status=True)
        return render(request, 'index.html', {'obj': obj})


@require_http_methods(["GET"])
def detail_class(request, program_id):
    if request.method == 'GET':
        program = Program.objects.get(program_id=program_id)
        obj = Class.objects.filter(class_program_id=program_id)
        return render(request, 'detail_class.html', {
            'obj': obj,
            'program': program,
            'program_id': program_id
        })


@require_http_methods(["GET"])
def about(request):
    if request.method == 'GET':
        about_data = About.objects.filter(about_status=True)
        return render(request, 'about.html', {
            'about_data': about_data
        })


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
