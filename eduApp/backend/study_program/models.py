from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Program(models.Model):
    class Meta:
        db_table = "program"

    program_id = models.AutoField(primary_key=True)
    program_updated_at = models.DateTimeField(auto_now=True)
    program_created_at = models.DateTimeField(auto_now_add=True)
    program_name = models.TextField(max_length=250, null=True, blank=True)
    program_detail = models.TextField(max_length=500, null=True, blank=True)
    program_status = models.BooleanField(null=True, blank=True, default=True)
    program_abbreviations = models.TextField(max_length=250, null=True, blank=True)
    program_user_created = models.ForeignKey(User, related_name='Cash_category_user_created', on_delete=models.SET_NULL, null=True, blank=True)
    program_user_updated = models.ForeignKey(User, related_name='Cash_category_user_updated', on_delete=models.SET_NULL, null=True, blank=True)
