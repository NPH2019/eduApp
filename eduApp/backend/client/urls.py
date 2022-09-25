from django.urls import path
from eduApp.backend.client import views

app_name = 'client'

urlpatterns = [
    path('', views.index, name='index-client'),
    path('create', views.create, name='create-client'),
    # path('tool', views.tool, name='create-tool')
]


