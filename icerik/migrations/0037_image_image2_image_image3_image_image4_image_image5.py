# Generated by Django 5.0 on 2023-12-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0036_rename_tasarimrehberkapak_teacher_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image2',
            field=models.ImageField(default='None', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='image',
            name='image3',
            field=models.ImageField(default='None', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='image',
            name='image4',
            field=models.ImageField(default='None', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='image',
            name='image5',
            field=models.ImageField(default='None', upload_to='images/'),
        ),
    ]
