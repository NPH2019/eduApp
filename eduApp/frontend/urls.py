from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('class', views.cls, name='class'),
    path('lesson', views.lesson, name='lesson'),
    path('contact', views.contact, name='contact'),
    path('login-client', views.login_client, name='login-client'),
    path('online-learning', views.learning, name='online-learning'),
    path('login-instructions', views.login_instructions, name='login-instructions'),
]
