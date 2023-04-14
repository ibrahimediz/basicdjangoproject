from django.urls import path,include 
from . import views

urlpatterns = [
    path('/liste',views.listele, name ="musterilistele")

]