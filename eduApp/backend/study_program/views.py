from django.shortcuts import render
from django.views.decorators.http import require_http_methods


# Create your views here.
# Programme
@require_http_methods(["GET"])
def programme(request):
    if request.method == 'GET':
        return render(request, 'programme/index.html')
