# Generated by Django 5.0 on 2023-12-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0035_image_alter_teacher_tasarimrehberkapak'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='tasarimrehberkapak',
            new_name='images',
        ),
    ]
