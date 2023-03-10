from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Products import products
from .models import Product


@api_view(['GET'])
def GetRoutes(request):
    routes = [

        '/api/products/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',


    ]

    return Response(routes)


@api_view(['GET'])
def GetProducts(requset):
    return Response(products)


@api_view(['GET'])
def GetProductById(requset, pk):
    product = None
    for i in products:
        if i["_id"] == pk:
            product = i
            break

    return Response(product)
