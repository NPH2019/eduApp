# Generated by Django 3.1.5 on 2022-01-08 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='program',
            fields=[
                ('program_id', models.AutoField(primary_key=True, serialize=False)),
                ('program_updated_at', models.DateTimeField(auto_now=True)),
                ('program_created_at', models.DateTimeField(auto_now_add=True)),
                ('program_name', models.TextField(blank=True, max_length=250, null=True)),
                ('program_detail', models.TextField(blank=True, max_length=500, null=True)),
                ('program_status', models.BooleanField(blank=True, default=True, null=True)),
                ('program_abbreviations', models.TextField(blank=True, max_length=250, null=True)),
                ('program_user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Cash_category_user_created', to=settings.AUTH_USER_MODEL)),
                ('program_user_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Cash_category_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'program',
            },
        ),
    ]
