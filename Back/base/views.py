from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import serializers


from .models import Product

class ProductSerializer(serializers.ModelSerializer):
   class Meta:
       model = Product
       fields = '__all__'

# Create your views here.
class manageProducts(APIView):
  def get(self, request, id=-1):  # axios.get
      if id > -1:
          my_model = Product.objects.get(id=id)
          serializer = ProductSerializer(my_model, many=False)
      else:
          my_model = Product.objects.all()
          serializer = ProductSerializer(my_model, many=True)
      return Response(serializer.data)




  def post(self, request):  # axios.post
      serializer = ProductSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




  def put(self, request, id):  # axios.put
      my_model = Product.objects.get(id=id)
      serializer = ProductSerializer(my_model, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




  def delete(self, request, id):  # axios.delete
      my_model = Product.objects.get(id=id)
      my_model.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)