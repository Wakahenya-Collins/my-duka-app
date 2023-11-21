from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.http import HttpResponse
from functools import wraps  
from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.views import View
from rest_framework.generics import ListCreateAPIView






class Views:
    # User views
    class YourView(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
    def my_function_based_view(request):
        # Your view logic here
        if request.method == 'GET':
            return HttpResponse("Hello, world!")
        else:
            return HttpResponse("Unsupported request method")
        
    class CategoryCreateView(View):
        def get(self, request):
            # Your view logic for handling GET requests here
            return HttpResponse("This is the product create page (GET)")

        def post(self, request):
            # Your view logic for handling POST requests here
            return HttpResponse("This is the product create page (POST)")
            
        
    class ProductCreateView(View):
        def get(self, request):
            # Your view logic for handling GET requests here
            return HttpResponse("This is the product create page (GET)")

        def post(self, request):
            # Your view logic for handling POST requests here
            return HttpResponse("This is the product create page (POST)")

    class ProductListView(generics.ListAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
    class CategoryListView(generics.ListAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
    class CategoryListView(ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer  # Make sure it's set to your CategorySerializer


    class ProductDetailView(generics.RetrieveAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

    # Admin views
    @user_passes_test(lambda u: u.is_staff, login_url='admin_login')  # Replace 'admin_login' with your admin login URL
    class ProductCreateView(generics.CreateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

    @user_passes_test(lambda u: u.is_staff, login_url='admin_login')  # Replace 'admin_login' with your admin login URL
    class ProductUpdateView(generics.UpdateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

    @user_passes_test(lambda u: u.is_staff, login_url='admin_login')  # Replace 'admin_login' with your admin login URL
    class ProductDeleteView(generics.DestroyAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer


    @staticmethod
    def admin_required(view_func):
        @wraps(view_func)
        def _checklogin(request, *args, **kwargs):  # Pass 'request' as a parameter
            if not request.user.is_staff:
                return redirect('account_login')  # Customize the redirect URL
            else:
                return view_func(request, *args, **kwargs)
        return _checklogin  # Return the inner function

    @staticmethod
    def permission_required(*perms):
        def check_perms(view_func):
            @wraps(view_func)
            def wrapped_view(request, *args, **kwargs):
                if not request.user.has_perms(perms):
                    return redirect('account_login')  # Customize the redirect URL
                else:
                    return view_func(request, *args, **kwargs)
            return wrapped_view
        return check_perms

    # For checking if the user is in the 'Admins' group
    @staticmethod
    def admin_group_required(view_func):
        def test(user):
            return user.groups.filter(name='Admins').exists()
        return user_passes_test(test)(view_func)



    class ProductListCreateView(generics.ListCreateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
    class CategoriesListCreateView(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
    class CategoriesListView(generics.ListCreateAPIView):
        queryset = Category.objects.all()
    serializer_class = CategorySerializer
    class CategoriesListCreateView(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = 'mydukaapp/products.html' 
    class CategoriesListView(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = 'mydukaapp/products.html' 


    class ProductListCreateView(generics.ListCreateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        template_name = 'mydukaapp/products.html'  


    class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
    
    def products_view(request):
        # Retrieve a list of products from the database
        products = Product.objects.all()

        # You can also implement pagination or filtering logic here if needed

        # Define the context to pass data to the template
        context = {
            'products': products,
        }

        # Render the 'products.html' template and pass the context data
        return render(request, 'products.html', context)
    def product_create_view(request):
        # Your view logic here
        if request.method == 'GET':
            # Logic for handling GET requests
            return HttpResponse("This is the product create page (GET)")
        elif request.method == 'POST':
            # Logic for handling POST requests
            return HttpResponse("This is the product create page (POST)")
        else:
            # Handle other HTTP methods if needed
            return HttpResponse("Unsupported request method")
    # views.py

    def category_list(request):
        categories = Category.objects.all()
        return render(request, 'category/category_list.html', {'categories': categories})

    def category_detail(request, category_id):
        category = Category.objects.get(pk=category_id)
        return render(request, 'category/category_detail.html', {'category': category})

    





