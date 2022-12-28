from rest_framework import serializers
from django.contrib. auth. models import User
from .models import Product

class ProductSerializer (serializers.Model Serializer) :
  class Meta:
    model=Product
    fields='_all'