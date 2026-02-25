from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Category, Product, Review
from .serializers import (
    CategoryDetailSerializer, CategoryListSerializer,
    ProductDetailSerializer, ProductListSerializer,
    ReviewDetailSerializer, ReviewListSerializer
)


@api_view(['GET'])
def category_detail_view(request, id):
    category = get_object_or_404(Category, id=id)
    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)

@api_view(['GET'])
def category_list_view(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_view(request, id):
    review = get_object_or_404(Review, id=id)
    serializer = ReviewDetailSerializer(review)
    return Response(serializer.data)

@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)