# Generated by Django 5.0 on 2023-12-12 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0002_teacher_onayli_mi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='secimalani',
        ),
    ]
