from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.listele,name="musterilistele"), # www.example.com/musteri
]

