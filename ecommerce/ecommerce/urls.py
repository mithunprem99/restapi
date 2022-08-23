"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from products import views
from rest_framework.authtoken.views import obtain_auth_token
# from .views import DetailCategory,ListCustomer,ListProduct,DetailProduct,ListCategory


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
     path('categories', views.ListCategory.as_view(), name='categories'),
    path('categories/<str:pk>/', views.DetailCategory.as_view(), name='singlecategory'),
    path('products/', views.ListProduct.as_view(), name='products'),
    path('products/<str:pk>/', views.DetailProduct.as_view(), name='singleproduct'),
    path('customer/', views.ListCustomer.as_view(), name='customer'),
    path('auth/',obtain_auth_token,name='obtainauth_token')

   
] 
