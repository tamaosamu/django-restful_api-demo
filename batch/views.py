from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .lib.bootstrap import Bootstrap

from .serv import Serv


class View(APIView):

    def get(self, request):
        Bootstrap(Serv())
        return Response([])
