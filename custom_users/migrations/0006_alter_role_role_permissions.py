# Generated by Django 5.0.6 on 2024-06-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0005_alter_customuser_user_roll_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_permissions',
            field=models.ManyToManyField(to='custom_users.permission'),
        ),
    ]
