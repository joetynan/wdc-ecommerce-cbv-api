from django.contrib import admin
from django.urls import path, include

from api import views

urlpatterns = [
    path('products/', views.ProductView.as_view()),
    path('products/<int:product_id>', views.ProductView.as_view())
    # write your URL rules here
]
