# Generated by Django 5.0 on 2023-12-18 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0027_alter_teacher_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['-created'], 'verbose_name_plural': 'İçerik Ekle'},
        ),
    ]