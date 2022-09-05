from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Program(models.Model):
    class Meta:
        db_table = "program"

    program_id = models.AutoField(primary_key=True)
    program_updated_at = models.DateTimeField(auto_now=True)
    program_created_at = models.DateTimeField(auto_now_add=True)
    program_code = models.TextField(max_length=250, null=True, blank=True)
    program_stt = models.TextField(max_length=250, null=True, blank=True)
    program_name = models.TextField(max_length=250, null=True, blank=True)
    program_detail = models.TextField(max_length=500, null=True, blank=True)
    program_status = models.BooleanField(null=True, blank=True, default=True)
    program_user_created = models.ForeignKey(User, related_name='Program_user_created', on_delete=models.SET_NULL, null=True, blank=True)
    program_user_updated = models.ForeignKey(User, related_name='Program_user_updated', on_delete=models.SET_NULL, null=True, blank=True)


class Class(models.Model):
    class Meta:
        db_table = "class"

    class_id = models.AutoField(primary_key=True)
    class_updated_at = models.DateTimeField(auto_now=True)
    class_created_at = models.DateTimeField(auto_now_add=True)
    class_code = models.TextField(max_length=250, null=True, blank=True)
    class_name = models.TextField(max_length=250, null=True, blank=True)
    class_detail = models.TextField(max_length=500, null=True, blank=True)
    class_status = models.BooleanField(null=True, blank=True, default=True)
    class_program = models.ForeignKey(Program, related_name='Class_program', on_delete=models.SET_NULL, null=True, blank=True)
    class_user_created = models.ForeignKey(User, related_name='Class_user_created', on_delete=models.SET_NULL, null=True, blank=True)
    class_user_updated = models.ForeignKey(User, related_name='Class_user_updated', on_delete=models.SET_NULL, null=True, blank=True)


class Topic(models.Model):
    class Meta:
        db_table = "topic"

    topic_id = models.AutoField(primary_key=True)
    topic_updated_at = models.DateTimeField(auto_now=True)
    topic_created_at = models.DateTimeField(auto_now_add=True)
    topic_code = models.TextField(max_length=250, null=True, blank=True)
    topic_name = models.TextField(max_length=250, null=True, blank=True)
    topic_detail = models.TextField(max_length=500, null=True, blank=True)
    topic_status = models.BooleanField(null=True, blank=True, default=True)
    topic_class = models.ForeignKey(Class, related_name='Topic_class', on_delete=models.SET_NULL, null=True, blank=True)
    topic_user_created = models.ForeignKey(User, related_name='Topic_user_created', on_delete=models.SET_NULL, null=True, blank=True)
    topic_user_updated = models.ForeignKey(User, related_name='Topic_user_updated', on_delete=models.SET_NULL, null=True, blank=True)


class Lesson(models.Model):
    class Meta:
        db_table = "lesson"

    lesson_id = models.BigAutoField(primary_key=True)
    lesson_files = models.FileField(upload_to='media/', max_length=500)
    lesson_updated_at = models.DateTimeField(auto_now=True)
    lesson_created_at = models.DateTimeField(auto_now_add=True)
    lesson_url = models.TextField(max_length=500, null=True, blank=True)
    lesson_view = models.TextField(max_length=10, null=True, blank=True)
    lesson_code = models.TextField(max_length=500, null=True, blank=True)
    lesson_name = models.TextField(max_length=500, null=True, blank=True)
    lesson_detail = models.TextField(max_length=500, null=True, blank=True)
    lesson_status = models.BooleanField(null=True, blank=True, default=True)
    lesson_evaluate = models.TextField(max_length=10, null=True, blank=True)
    lesson_download = models.TextField(max_length=500, null=True, blank=True)
    lesson_topic = models.ForeignKey(Topic, related_name='Lesson_topic', on_delete=models.SET_NULL, null=True, blank=True)
    lesson_user_created = models.ForeignKey(User, related_name='Lesson_user_created', on_delete=models.SET_NULL, null=True, blank=True)
    lesson_user_updated = models.ForeignKey(User, related_name='Lesson_user_updated', on_delete=models.SET_NULL, null=True, blank=True)
