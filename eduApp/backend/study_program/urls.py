from django.urls import path
from eduApp.backend.study_program import views

app_name = 'study-program'

urlpatterns = [
    # class
    path('class', views.ad_class, name='class'),
    # lesson
    path('lesson', views.lesson, name='lesson'),
    # topic
    path('topic', views.topic, name='topic'),
    # program
    path('program', views.program, name='program'),

    # create class
    path('class-create', views.ad_class_create, name='class-create'),
    # create lesson
    path('lesson-create', views.lesson_create, name='lesson-create'),
    # create topic
    path('topic-create', views.topic_create, name='topic-create'),
    # create program
    path('program-create', views.program_create, name='program-create'),
]

