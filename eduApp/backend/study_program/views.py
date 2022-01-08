from .forms import ProgramCreateForm
from .models import Program
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods


# Create your views here.
# Class
@require_http_methods(["GET"])
def ad_class(request):
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
        obj = Program.objects.all()
        return render(request, 'programme/index.html', {'obj': obj})


# Programme create
@require_http_methods(["GET", "POST"])
def programme_create(request):
    if request.method == 'POST':
        forms_update = ProgramCreateForm(request.POST)
        if forms_update.is_valid():
            program_name = request.POST['program_name']
            program_detail = request.POST['program_detail']
            program_abbreviations = request.POST['program_abbreviations']

            if 'program_status' in request.POST:
                program_status = request.POST['program_status']
                if program_status != '':
                    program_status = True
            else:
                program_status = False
            obj = Program()
            obj.program_name = program_name
            obj.program_detail = program_detail
            obj.program_status = program_status

            obj.program_abbreviations = program_abbreviations
            obj.save()
            return redirect('study-program:programme')

    return render(request, 'programme/create.html')
