# Generated by Django 5.0 on 2023-12-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0029_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='pdf_file',
            field=models.FileField(blank=True, default='None', null=True, upload_to='pdfs/'),
        ),
    ]
