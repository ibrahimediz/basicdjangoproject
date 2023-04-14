from django.db import models
from django.utils import timezone

class MusteriModel(models.Model):
    class Meta:
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"

    adi = models.CharField(max_length=50,verbose_name="Adı")
    soyadi = models.CharField(max_length=50,verbose_name="SOYADI")
    eposta = models.EmailField(max_length=254,verbose_name="E-POSTA")
    adres = models.TextField(verbose_name="ADRES")
    kayit_zaman = models.DateTimeField(default=timezone.now,verbose_name="KAYIT ZAMANI")

    def __str__(self):
        return self.adi + " " + self.soyadi
    