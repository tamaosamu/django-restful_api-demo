# Create your views here.
"""_summary_

Returns:
    _type_: _description_
"""
from django.http import JsonResponse

# from django.core import serializers
from .models import Book, Info
from .serializer import BookSerializer, InfoSerializer, ArticleSerializer


def index(self):
    """_summary_

    Returns:
        _type_: _description_
    """
    return JsonResponse({})


def one_to_one_user(self):
    """_summary_

    Returns:
        _type_: _description_
    """
    book = Book.objects.get(pk=2)
    book_serializer = BookSerializer(book)
    # print(user)
    info_serializer = InfoSerializer(book.info)
    data = {**book_serializer.data, **info_serializer.data}
    print(data)
    # data = serializers.serialize("json", data)
    return JsonResponse(data)


def one_to_one_userext(self):
    """_summary_

    Returns:
        _type_: _description_
    """
    info = Info.objects.get(pk=1)
    data = InfoSerializer(info).data
    return JsonResponse(data)


def one_to_many_article(self):
    """_summary_"""

    book = Book.objects.get(pk=2)
    book_serializer = BookSerializer(book)
    articles_serializer = ArticleSerializer(book.articles.all(), many=True)
    data = {**book_serializer.data, "articles": articles_serializer.data}
    return JsonResponse(data)


from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(["GET"])
def hello_world(request: Request):
    return Response({"message": "Hello, world!"})
