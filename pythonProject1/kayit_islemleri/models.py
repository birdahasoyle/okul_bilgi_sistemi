from django.db import models

# Create your models here.


class Kayit_Turu(models.Model):
    tur = models.CharField(max_length=50)

    def __str__(self):
        return self.tur


class Sehir(models.Model):
    sehir_adi = models.CharField(max_length=50)

    def __str__(self):
        return self.sehir_adi


class Okul(models.Model):
    sehir = models.ForeignKey(Sehir, on_delete=models.CASCADE, verbose_name='Sehir')
    kayit_turu = models.ForeignKey(Kayit_Turu, on_delete=models.CASCADE, verbose_name='Kayit Turu')
    isim_soyisim = models.CharField(max_length=50, verbose_name='Isim Soyisim')
    telefon = models.BigIntegerField(verbose_name='Telefon')

    class Meta:
        db_table = 'kayit_islemleri_okul'

    def __str__(self):
        return self.isim_soyisim


