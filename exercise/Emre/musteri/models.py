from django.db import models
from django.utils import timezone

class MusteriModel(models.Model):
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=50)
    eposta = models.EmailField(max_length=254)
    adres = models.TextField()
    kayit_zaman = models.DateTimeField(default=timezone.now)