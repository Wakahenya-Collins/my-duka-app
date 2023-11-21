"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from mydukaapp.views import Views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static



router = DefaultRouter()


urlpatterns = [
    path('my-view/', Views.my_function_based_view, name='my-view'),
    path('products/', Views.products_view, name='products'),
    path('api/products/', Views.ProductListView.as_view(), name='product-list'),
    path('categories/', Views.category_list, name='categories'),
    path('api/categories/', Views.CategoriesListView.as_view(), name='category-list'),
    path('api/products/<int:pk>/', Views.ProductDetailView.as_view(), name='product-detail'),
    path('api/products/create/', Views.ProductCreateView, name='product-create'),
    path('api/categories/', Views.category_list, name='category_list'),
    path('categories/<int:category_id>/', Views.category_detail, name='category_detail'),
    # path('admin/products/create/', Views.ProductCreateView.as_view(), name='product-create'),
    path('admin/products/update/<int:pk>/', Views.ProductUpdateView, name='product-update'),
    path('admin/products/delete/<int:pk>/', Views.ProductDeleteView, name='product-delete'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
