# Generated by Django 5.0 on 2023-12-12 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0003_remove_teacher_secimalani'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='onayli_mi',
        ),
    ]