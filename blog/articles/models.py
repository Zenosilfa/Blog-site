from tabnanny import verbose
from django.db import models
from sympy import content
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")
    article_image = models.FileField(blank=True,null=True,verbose_name = "Dosya Ekleyin")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="makale",related_name="comments")
    comment_author = models.CharField(max_length=20,verbose_name="İsim...")
    comment_content = models.CharField(max_length=5000,verbose_name="yorum...")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Tarih")
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-created_date']