from django.db import models

# Create your models here.

class resim(models.Model):
    resim1 = models.ImageField(upload_to='resim/', blank = True, null = True)

    def __str__(self):
        return str(self.resim1)

class kategori(models.Model):
    kategori_isim = models.CharField(max_length=100)
    kategori_resim = models.FileField(upload_to ='resim/', blank = True, null = True, verbose_name="resimler")

    def __str__(self):
        return str(self.kategori_resim)