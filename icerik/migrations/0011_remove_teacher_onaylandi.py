# Generated by Django 5.0 on 2023-12-12 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0010_alter_teacher_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='onaylandi',
        ),
    ]