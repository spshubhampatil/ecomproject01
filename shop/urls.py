from django.contrib import admin
from django.urls import path, include
from .views.index import index
from .views.product import productdetails
from shop.views.signup import SignupView

urlpatterns = [    
    path('', index, name="index"),
    path('product', productdetails, name="productdetails"),
    path('signup',SignupView.as_view(), name="signup"),
]