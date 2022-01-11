from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from eduApp.backend.account.forms import LoginForm


@login_required(login_url='login')
@require_http_methods(["GET"])
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html')


def signin(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if not request.POST.get('remember_me', None):
                    request.session.set_expiry(0)

                return redirect('/admin')
            else:
                login_form.add_error(None, 'Tài khoản hoặc mật khẩu không đúng')
    else:
        if request.user.is_authenticated:
            return redirect('/admin')
        else:
            login_form = LoginForm()

    return render(request, 'authen/login.html', {
        'login_form': login_form
    })


def signout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')