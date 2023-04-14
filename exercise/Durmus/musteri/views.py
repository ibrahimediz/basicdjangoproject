from django.shortcuts import render

# Create your views here.

def listele(request):
    return render(request,"musteri/musteriliste.html")