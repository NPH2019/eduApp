from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('sell_card', views.sell_card, name='sell_card'),
    path('search', views.search, name='search'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('class/<int:class_id>', views.cls, name='class'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('lesson/<int:lesson_id>', views.lesson, name='lesson'),
    path('login-client', views.login_client, name='login-client'),
    path('program/<int:program_id>', views.program, name='program'),
    path('online-learning', views.learning, name='online-learning'),
    path('login-instructions', views.login_instructions, name='login-instructions'),
]


