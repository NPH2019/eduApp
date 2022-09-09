from django.urls import path
from eduApp.backend.card import views

app_name = 'card'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('update/<int:card_id>', views.card_update, name='card-update'),
    path('delete/<int:card_id>', views.card_delete, name='card-delete'),
]