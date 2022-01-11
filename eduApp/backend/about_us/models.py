from django.db import models
from django.contrib.auth.models import User


class About(models.Model):
    class Meta:
        db_table = "about"

    about_id = models.AutoField(primary_key=True)
    about_description = models.TextField(max_length=500, null=True, blank=True)
    about_enable = models.BooleanField(null=True, blank=True, default=True)
    about_status = models.BooleanField(null=True, blank=True, default=True)
    about_user_created = models.ForeignKey(
        User, related_name='about_user_created',
        on_delete=models.SET_NULL, null=True, blank=True
    )
    about_user_updated = models.ForeignKey(
        User, related_name='about_user_updated',
        on_delete=models.SET_NULL, null=True, blank=True
    )
    about_created_at = models.DateTimeField(auto_now_add=True)
    about_updated_at = models.DateTimeField(auto_now=True)