# Generated by Django 5.0 on 2023-12-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0011_remove_teacher_onaylandi'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='onayli',
            field=models.BooleanField(default=False),
        ),
    ]
