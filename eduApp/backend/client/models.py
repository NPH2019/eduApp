from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserClient(models.Model):
    class Meta:
        db_table = 'client'

    client_id = models.BigAutoField(primary_key=True)
    client_updated_at = models.DateTimeField(auto_now=True)
    client_end_date = models.DateField(null=True, blank=True)
    client_password = models.TextField(null=False, blank=True)
    client_start_date = models.DateField(null=True, blank=True)
    client_created_at = models.DateTimeField(auto_now_add=True)
    client_mail = models.TextField(max_length=50, null=True, blank=True)
    client_code = models.TextField(max_length=100, null=True, blank=True)
    client_address = models.TextField(max_length=500, null=True, blank=True)
    client_name = models.TextField(max_length=100, null=False, blank=True)
    client_status = models.BooleanField(null=True, blank=True, default=True)
    client_user_created = models.ForeignKey(User, related_name='Client_user_created', on_delete=models.SET_NULL, null=True, blank=True)
    client_user_updated = models.ForeignKey(User, related_name='Client_user_updated', on_delete=models.SET_NULL, null=True, blank=True)
