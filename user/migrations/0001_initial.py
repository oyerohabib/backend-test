# Generated by Django 5.1.1 on 2024-09-15 11:23

import common.kgs
import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.CharField(default=common.kgs.generate_unique_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('code', models.CharField(db_index=True, max_length=255, unique=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.CharField(default=common.kgs.generate_unique_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=600, null=True)),
                ('firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=17, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='user_images/')),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Student', 'Student'), ('SuperAdmin', 'SuperAdmin')], max_length=100)),
                ('matric_no', models.CharField(db_index=True, max_length=255, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('verified', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='user.department')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='EligibleUserUpload',
            fields=[
                ('id', models.CharField(default=common.kgs.generate_unique_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='users/bulk')),
                ('number_of_valid', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('number_of_invalid', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('total_upload', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('error_file', models.FileField(blank=True, null=True, upload_to='users/bulk')),
                ('status', models.CharField(choices=[('Started', 'Started'), ('Completed', 'Completed')], default='Started', max_length=100)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=255, null=True)),
                ('token_type', models.CharField(choices=[('LoginToken', 'LoginToken')], default='LoginToken', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
