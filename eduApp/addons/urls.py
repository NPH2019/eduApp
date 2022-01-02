from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from eduApp.addons import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='dashboard'),
]