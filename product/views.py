from itertools import product
from math import prod
from tkinter.messagebox import NO
from xml.parsers.expat import model
from django.shortcuts import render
from django.http import Http404
from .models import Products
from .serializers import ProductsSerializer

# rest dependencies import
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class AllProducts(APIView):
    model = Products
    serializer = ProductsSerializer

    def get(self, request, format=None, *args, **kwargs):
        all_products = self.model.objects.all()
        serializer = self.serializer(all_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        product_data = serializer.data
        response = {
            'data': {
                'product': dict(product_data),
                'status': 'Success',
                'response': 'The new product has been uploaded successfully!'
            }
        }

        return Response(response, status=status.HTTP_201_CREATED)


class SingleProduct(APIView):
    model = Products
    serializer = ProductsSerializer

    def get_product_by_pk(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None, *args, **kwargs):
        product = self.get_product_by_pk(pk)
        serializer = self.serializer(product)

        return Response(serializer.data)

    def put(self, request, pk, format=None, *args, **kwargs):
        product = self.get_product_by_pk(pk)
        serializer = self.serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        product = self.get_product_by_pk(pk)
        product.delete()
        return Response(status=status.HTTP_200_OK)
