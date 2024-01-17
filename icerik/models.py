from django.db import models
import os
from natsort import natsorted
from zipfile import ZipFile
from django.conf import settings
from ckeditor.fields import RichTextField

class Teacher(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name="İçerik Kapak Fotoğrafı")
    icerikanabaslik = models.CharField(default="Buraya İçeriğin Ana Başlığı Giriniz!",max_length=100, verbose_name="İçerik Ana Başlığı")
    icerikbaslik = models.CharField(default="Hazırla", max_length=100, verbose_name="Hazırla Bölüm Başlığı")
    icerikyazi = RichTextField(verbose_name="Hazırla Bölüm İçeriği")
    icerikbaslik2 = models.CharField(default="İlgi Uyandırma",max_length=100, verbose_name="İlgi Uyandırma Bölüm Başlığı")
    icerikyazi2 = RichTextField(verbose_name="İlgi Uyandırma Bölüm İçeriği")
    icerikbaslik3 = models.CharField(default="Keşfet ve Deneyimle",max_length=100, verbose_name="Keşfet ve Deneyimle Bölüm Başlığı")
    icerikyazi3 = RichTextField(verbose_name="Keşfet ve Deneyimle Bölüm İçeriği")
    icerikbaslik4 = models.CharField(default="Keşfet ve Tasarla",max_length=100, verbose_name="Keşfet ve Tasarla Bölüm Başlığı")
    icerikyazi4 = RichTextField(verbose_name="Keşfet ve Tasarla Bölüm İçeriği")
    icerikbaslik5 = models.CharField(default="Kodla ve Deneyimle",max_length=100, verbose_name="Kodla ve Deneyimle Bölüm Başlığı")
    icerikyazi5 = RichTextField(verbose_name="Kodla ve Deneyimle Bölüm İçeriği")
    icerikbaslik6 = models.CharField(default="Farklılaştırma",max_length=100, verbose_name="Farklılaştırma Bölüm Başlığı")
    icerikyazi6 = RichTextField(verbose_name="Farklılaştırma Bölüm İçeriği")
    icerikbaslik7 = models.CharField(default="Eklenti",max_length=100, verbose_name="Eklenti Bölüm Başlığı")
    icerikyazi7 = RichTextField(verbose_name="Eklenti Bölüm İçeriği")
    video = models.FileField(upload_to='videos/', default="None", verbose_name="MP4 Video" )
    tasarimrehberkapak = models.FileField(upload_to='images/kod/kapak/', default="None", verbose_name="Kod Rehber Kapağı")
    kodrehberkapak = models.FileField(upload_to='images/kod/kapak/', default="None", verbose_name="Kod Rehber Kapağı")
    ZORLUK = [
        ('Basit','Basit'),
        ('Orta','Orta'),
        ('Zor','Zor'),
    ]
    SINIF = [
        ('Okul Öncesi', 'Okul Öncesi'),
        ('1-2. Sınıf', '1-2. Sınıf'),
        ('1-8. Sınıf', '1-5. Sınıf'),
        ('6-8. Sınıf', '6-8. Sınıf'),
        ('Tüm Sınıflar', 'Tüm Sınıflar'),
    ]
    derece = models.CharField(max_length=20, choices=ZORLUK, verbose_name="Zorluk Derecesi")
    sinif = models.CharField(max_length=20, choices=SINIF, default='Okul Öncesi', verbose_name="Sınıf Aralığı")
    sure = models.CharField(default="45",max_length=3, verbose_name="Ders Süresi")
    onayli = models.BooleanField(default=False, verbose_name="Öğretmen İçerik Onayı!")
    onaylimi = models.BooleanField(default=False, verbose_name="Öğrenci İçerik Onayı!")
    is_new = models.BooleanField(default=False, verbose_name="YENİ İÇERİK İSE TİK AT, HER YENİ İÇERİK EKLENDİĞİNDE ÖNCEKİ KALDIRILMALI!")  # Yeni içerik belirleyici alanı
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    uyumlupinooveset = RichTextField(verbose_name="Uyumlu Pinoo Kartlar Ve Lego Setleri", blank=True, null=True)
    gereklimateryal = RichTextField(verbose_name="Gerekli Materyaller İçeriği", blank=True, null=True)
    ekkaynak = RichTextField(verbose_name="Ek kaynak İçeriği", blank=True, null=True)
    
    
    zip_file = models.FileField(upload_to='uploads/', blank=True, null=True)

    def extract_images(self):
        if self.zip_file:
            zip_path = os.path.join(settings.MEDIA_ROOT, str(self.zip_file))
            images = []

            with ZipFile(zip_path, 'r') as zip_ref:
                for file_name in zip_ref.namelist():
                    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        zip_ref.extract(file_name, os.path.join(settings.MEDIA_ROOT, 'uploads'))
                        images.append(os.path.join('uploads/', file_name))

            return images
        return []
    

    custom_zip_file = models.FileField(upload_to='custom_uploads/', blank=True, null=True)

    def extract_custom_images(self):
        if self.custom_zip_file:
            zip_path = os.path.join(settings.MEDIA_ROOT, str(self.custom_zip_file))
            custom_images = []

            with ZipFile(zip_path, 'r') as zip_ref:
                for file_name in zip_ref.namelist():
                    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        zip_ref.extract(file_name, os.path.join(settings.MEDIA_ROOT, 'custom_uploads'))
                        custom_images.append(os.path.join('custom_uploads/', file_name))

            return custom_images
        return []

    class Meta:
        verbose_name_plural = "İçerik Ekle" 
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if self.pk is None:  # Yeni bir öğe eklendiğinde
            self.is_new = True  # is_new alanını True yap
        super().save(*args, **kwargs)


    def __str__(self):
        return self.icerikanabaslik

class URL(models.Model):
    name = models.CharField(max_length=50,default="URL'yi Buradan Değiştir!") 
    pinoostudio = models.URLField(blank=True, null=True)
    pinoocode = models.URLField(blank=True, null=True)
    windows = models.URLField(blank=True, null=True)
    linux = models.URLField(blank=True, null=True)
    macos = models.URLField(blank=True, null=True)
    ios = models.URLField(blank=True, null=True)
    google = models.URLField(blank=True, null=True)
    android = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name