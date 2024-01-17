# Generated by Django 5.0 on 2023-12-27 09:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0042_teacher_onaylimi'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='ekkaynak',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ek kaynak İçeriği'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='gereklimateryal',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Gerekli Materyaller İçeriği'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='uyumlupinooveset',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Uyumlu Pinoo Kartlar Ve Lego Setleri'),
        ),
    ]
