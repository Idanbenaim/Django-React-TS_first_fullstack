from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
  path('products/<int:id>',views.manageProducts.as_view()),
  path('products/', views.manageProducts.as_view()),
]

