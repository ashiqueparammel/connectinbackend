from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.

from rest_framework.decorators import api_view

@api_view(['GET'])
def check(request):
    data = {'message': 'Hello, world!'}
    return Response(data)

    