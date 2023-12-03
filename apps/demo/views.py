from django.shortcuts import render

from django.http import HttpResponse
from django.db import connection
from .models import XUser
from faker import Faker

fake = Faker(locale='zh_CN')

def index(request):
    
    userFields = XUser._meta.fields
    
# BigAutoField CharField IntegerField DateField BooleanField
    list = []
    for field in userFields:
        #print(field)
        type_name = type(field).__name__
        field_name = field.__str__
        list.append((type_name, field_name))
    
    return HttpResponse("hello world111")
