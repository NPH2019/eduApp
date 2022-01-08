from django.urls import path
from eduApp.backend.study_program import views

app_name = 'study-program'

urlpatterns = [
    # class
    path('class', views.ad_class, name='class'),
    # lesson
    path('lesson', views.lesson, name='lesson'),
    # subject
    path('subject', views.subject, name='subject'),
    # Programme
    path('programme', views.programme, name='programme'),
    # Programme create
    path('programme-create', views.programme_create, name='programme-create'),
]

