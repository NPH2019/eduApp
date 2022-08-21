from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.crypto import get_random_string
from django.views.decorators.http import require_http_methods

from eduApp.backend.client.forms import ClientCreateForm
from eduApp.backend.client.models import UserClient


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == 'GET':
        return render(request, 'user_client/index.html')


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        forms = ClientCreateForm(request.POST)
        if forms.is_valid():
            if request.POST['amount'] and request.POST['end-date']:
                max_row = request.POST['amount']
                for row in range(1, int(max_row) + 1):
                    obj = UserClient()
                    obj.client_name = get_random_string(length=8)
                    obj.client_password = get_random_string(length=8)
                    obj.client_code = request.POST['code']
                    obj.client_start_date = datetime.now()
                    obj.client_end_date = request.POST['end-date']
                    obj.client_status = 1
                    obj.save()
        return redirect('client:index-client')

    return render(request, 'user_client/create.html')
