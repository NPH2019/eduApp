from django.urls import path

from eduApp.backend import views

app_name = 'backend'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]