# MVC Model view component
# MTV Model Template view = Bu bizim kullandığımız yöntem
# Flux
# Micro Servis
from django.shortcuts import render
from .models import *


# Create your views here.
def indexPage(request):
    context = {}
    
    blogs = BlogModel.objects.all()
    
    
    
    # SELECT * FROM BlogModel;
    context['all_blogs'] = blogs
    return render(request, 'index.html',context)



def blogDetail(request):
    return render(request, 'blogDetay.html')