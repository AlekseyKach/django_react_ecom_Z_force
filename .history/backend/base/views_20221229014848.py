from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Products import products
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def getRoutes(request):
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
def getProducts(requset):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(products)


@api_view(['GET'])
def getProductById(requset, pk):
    product = None
    for i in products:
        if i["_id"] == pk:
            product = i
            break

    return Response(product)
