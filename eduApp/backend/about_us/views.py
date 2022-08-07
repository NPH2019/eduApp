from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .models import About
from eduApp.backend.about_us.forms import AboutForm


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == 'GET':
        return render(request, 'about/index.html')


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def create(request):
    if request.is_ajax and request.method == "POST":
        obj_about = About()
        about_data = request.POST.get("textareaValue", None)
        obj_about.about_description = about_data
        obj_about.save()
    return render(request, 'about/create.html')

