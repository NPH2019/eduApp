from django.urls import path

from eduApp.backend.account import views

app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]