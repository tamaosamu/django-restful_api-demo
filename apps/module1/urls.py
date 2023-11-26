from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user", views.one_to_one_user, name="oneToOneUser"),
    path("userext", views.one_to_one_userext, name="oneToOneUserExt"),
    path("userarticle", views.one_to_many_article, name="oneToManyArticle"),
    path("test", views.hello_world, name="helloWorld"),
]
