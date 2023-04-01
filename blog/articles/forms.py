from pyexpat import model

from django.forms import ModelForm

from articles.models import Article
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','content',"article_image"]