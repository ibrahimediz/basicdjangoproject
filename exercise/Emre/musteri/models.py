from django.db import models
from django.utils import timezone

class MusteriModel(models.Model):
    class Meta:
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"


    adi = models.CharField(max_length=50, verbose_name="Adı")
    soyadi = models.CharField(max_length=50, verbose_name="Soyadı")
    eposta = models.EmailField(max_length=254)
    adres = models.TextField()
    kayit_zaman = models.DateTimeField(default=timezone.now, verbose_name="Kayıt zamanı")

    def __str__(self):
        return self.adi + " " + self.soyadi