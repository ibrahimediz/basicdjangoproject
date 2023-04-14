from django.shortcuts import render

def listele(request):
    return render(request,"musteri/listele.html",{})