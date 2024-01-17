# Generated by Django 4.2.7 on 2023-12-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('icerikanabaslik', models.CharField(default='Buraya İçeriğin Ana Başlığı Giriniz!', max_length=100)),
                ('icerikbaslik', models.CharField(default='Hazırla', max_length=100)),
                ('icerikyazi', models.TextField()),
                ('icerikbaslik2', models.CharField(default='İlgi Uyandırma', max_length=100)),
                ('icerikyazi2', models.TextField()),
                ('icerikbaslik3', models.CharField(default='Keşfet ve Deneyimle', max_length=100)),
                ('icerikyazi3', models.TextField()),
                ('icerikbaslik4', models.CharField(default='Keşfet ve Tasarla', max_length=100)),
                ('icerikyazi4', models.TextField()),
                ('icerikbaslik5', models.CharField(default='Kodla ve Deneyimle', max_length=100)),
                ('icerikyazi5', models.TextField()),
                ('icerikbaslik6', models.CharField(default='Farklılaştırma', max_length=100)),
                ('icerikyazi6', models.TextField()),
                ('icerikbaslik7', models.CharField(default='Eklenti', max_length=100)),
                ('icerikyazi7', models.TextField()),
                ('video', models.FileField(default='None', upload_to='videos/')),
                ('tasarimrehberkapak', models.ImageField(default='None', upload_to='images/tasarim/kapak/')),
                ('kodrehberkapak', models.ImageField(default='None', upload_to='images/kod/kapak/')),
                ('derece', models.CharField(choices=[('Basit', 'Basit'), ('Orta', 'Orta'), ('Zor', 'Zor')], default='Basit', max_length=20)),
                ('sinif', models.CharField(choices=[('Okul Öncesi', 'Okul Öncesi'), ('1-2. Sınıf', '1-2. Sınıf'), ('1-8. Sınıf', '1-5. Sınıf'), ('6-8. Sınıf', '6-8. Sınıf'), ('Tüm Sınıflar', 'Tüm Sınıflar')], default='Okul Öncesi', max_length=20)),
                ('sure', models.CharField(default='45', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('icerikanabaslik', models.CharField(default='Buraya İçeriğin Ana Başlığı Giriniz!', max_length=100)),
                ('icerikbaslik', models.CharField(default='Hazırla', max_length=100)),
                ('icerikyazi', models.TextField()),
                ('icerikbaslik2', models.CharField(default='İlgi Uyandırma', max_length=100)),
                ('icerikyazi2', models.TextField()),
                ('icerikbaslik3', models.CharField(default='Keşfet ve Deneyimle', max_length=100)),
                ('icerikyazi3', models.TextField()),
                ('icerikbaslik4', models.CharField(default='Keşfet ve Tasarla', max_length=100)),
                ('icerikyazi4', models.TextField()),
                ('icerikbaslik5', models.CharField(default='Kodla ve Deneyimle', max_length=100)),
                ('icerikyazi5', models.TextField()),
                ('icerikbaslik6', models.CharField(default='Farklılaştırma', max_length=100)),
                ('icerikyazi6', models.TextField()),
                ('icerikbaslik7', models.CharField(default='Eklenti', max_length=100)),
                ('icerikyazi7', models.TextField()),
                ('video', models.FileField(default='None', upload_to='videos/')),
                ('tasarimrehberkapak', models.ImageField(default='None', upload_to='images/kapak/')),
                ('kodrehberkapak', models.ImageField(default='None', upload_to='images/kod/kapak/')),
                ('derece', models.CharField(choices=[('Basit', 'Basit'), ('Orta', 'Orta'), ('Zor', 'Zor')], max_length=20)),
                ('sinif', models.CharField(choices=[('Okul Öncesi', 'Okul Öncesi'), ('1-2. Sınıf', '1-2. Sınıf'), ('1-8. Sınıf', '1-5. Sınıf'), ('6-8. Sınıf', '6-8. Sınıf'), ('Tüm Sınıflar', 'Tüm Sınıflar')], default='Okul Öncesi', max_length=20)),
                ('sure', models.CharField(default='45', max_length=3)),
                ('secimalani', models.ManyToManyField(blank=True, to='icerik.tag')),
            ],
        ),
    ]
