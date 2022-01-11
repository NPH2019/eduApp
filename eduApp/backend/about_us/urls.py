from django.urls import path
from eduApp.backend.about_us import views

app_name = 'about_us'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
]