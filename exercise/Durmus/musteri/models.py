from django.db import models
from django.utils import timezone

# Create your models here.
class MusteriModel(models.Model):
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=50)
    eposta = models.EmailField(max_length=254)
    adres = models.TextField()
    kayit_zaman = models.DateTimeField(default=timezone.now)
    
