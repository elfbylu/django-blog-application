# MVC Model view component
# MTV Model Template view = Bu bizim kullandığımız yöntem
# Flux
# Micro Servis
from django.shortcuts import render ,redirect
from .models import *


# Create your views here.
def indexPage(request):
    context = {}
    
    if request.method == "POST":
        
        postAuthor = request.POST.get('post_author')
        postIcerik = request.POST.get('post_içerik')
        postresim = request.POST.get('post_içerik_resim')
        
        print("GELEN VERİLER: ",postIcerik,postresim)
        #gelen veriyi veri tabanıbna kaydet
        BlogModel.objects.create(author = postAuthor,post = postIcerik)
        #anasayfaya geri gönder
        return redirect('home-view')
    else:
    
         blogs = BlogModel.objects.all().order_by("-createdit")
    
    
    
         # SELECT * FROM BlogModel;
         context['all_blogs'] = blogs
         
         return render(request, 'index.html',context)


#  blog detay sayfası 
def blogDetail(request):
    return render(request, 'blogDetay.html')



# blog sil
def blogDelete(request,blogId):
    
# modeli bul
    blog = BlogModel.objects.filter(id = int(blogId)).first()
  
    if blog:
        blog.delete()
    # başarılı mesaj yazdır
    else:
    # hata mesajı yazdır
        pass
        
        
        
    # tekrara anasayfaya yönlendir
    return redirect('home-view')


   # blog güncelle
def blogUpdate(request,blogId):
       context = {}
       
       blog = BlogModel.objects.filter(id = int(blogId)).first()
       
       
       if blog:
           context['blog'] = blog
           
       else:
           context['blog'] = None
       
       if request.method == 'POST':
           
           author = request.POST.get('blogAuthor')
           post = request.POST.get('blogPost')
           
           blog.post = post
           blog.author = author
           # veritabanına kaydet
           blog.save()
           
           # aynı sayfaya yönlendir
           return redirect("blog-update-view",blog.id)
           
       else:    
         return render(request,'updateBlog.html', context)