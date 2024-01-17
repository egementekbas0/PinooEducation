# Generated by Django 5.0 on 2023-12-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icerik', '0034_teacher_tasarimrehberkapak'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tasarimrehberkapak',
            field=models.ManyToManyField(to='icerik.image'),
        ),
    ]
