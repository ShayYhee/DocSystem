# Generated by Django 5.1.7 on 2025-05-23 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0018_notification_today'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='today',
        ),
    ]
