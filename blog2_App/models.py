from django.db import models
from datetime import datetime

# Create your models here.
class BlogModel(models.Model):
    # Gizli bir id'i vardır
    # model.py da yapılan her değişiklikten sonra py manage.py makemigrations daha sonra migrate yapılmalı
    # field (alow)
    author = models.CharField(("Yazar"), max_length=50)
    post = models.TextField(("Post İçerik"))
    attachament = models.ImageField(("Görsel"), upload_to=None, blank=True)
    createdit = models.DateTimeField(("Tarih"), auto_now=True)
    updateAt = models.DateTimeField(("Güncelleme Tarihi"), auto_now_add=True, blank=True,null=True)
    
    
    def __str__(self) -> str:
        return self.post