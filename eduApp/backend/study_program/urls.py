from django.urls import path
from eduApp.backend.study_program import views

app_name = 'study-program'

urlpatterns = [
    # Programme
    path('', views.programme, name='programme'),
]
