# MVC Model view component
# MTV Model Template view = Bu bizim kullandığımız yöntem
# Flux
# Micro Servis
from django.shortcuts import render


# Create your views here.
def indexPage(request):
    return render(request, 'index.html')



def blogDetail(request):
    return render(request, 'blogDetay.html')