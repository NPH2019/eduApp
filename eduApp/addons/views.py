from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
from django.shortcuts import render


@require_http_methods(["GET"])
def index(request):
    return render(request, 'index.html')