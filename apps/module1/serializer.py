from rest_framework import serializers
from .models import Book, Info, Article

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name',"age", 'id')
       

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ("nickname","brithday", "id")
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "pub_date", "id")
        