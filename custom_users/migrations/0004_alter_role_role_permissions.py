# Generated by Django 5.0.6 on 2024-06-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0003_remove_permission_roles_role_role_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_permissions',
            field=models.ManyToManyField(related_name='permissions', to='custom_users.permission'),
        ),
    ]
