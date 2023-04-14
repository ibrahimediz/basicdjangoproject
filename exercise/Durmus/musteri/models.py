from django.db import models
from django.utils import timezone

# Create your models here.
class MusteriModel(models.Model):
    class Meta:
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"

    
    adi = models.CharField(max_length=50,verbose_name="ADI")
    soyadi = models.CharField(max_length=50,verbose_name="SOYADI")
    eposta = models.EmailField(max_length=254,verbose_name="E-POSTA")
    adres = models.TextField()
    kayit_zaman = models.DateTimeField(default=timezone.now, verbose_name="KAYIT ZAMANI")
    
    def __str__(self):
        return self.adi+" "+self.soyadi

    
