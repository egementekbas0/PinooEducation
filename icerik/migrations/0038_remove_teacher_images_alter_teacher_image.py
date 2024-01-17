# Generated by Django 5.0 on 2023-12-25 10:55

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0037_image_image2_image_image3_image_image4_image_image5'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='images',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='teachers/'),
        ),
    ]
