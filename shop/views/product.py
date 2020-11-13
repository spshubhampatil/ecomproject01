from django.shortcuts import render
# from shop.models import Product,ProductImage, User, Payment
from django.db.models import Q


def productdetails(request):
    return render(request,'product_details.html')