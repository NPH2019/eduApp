from django.urls import path
from eduApp.backend.card import views

app_name = 'card'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
]