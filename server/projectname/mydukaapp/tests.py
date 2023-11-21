from django.test import TestCase
from django.urls import reverse


# Create your tests here.from django.test import TestCase
from .models import CustomUser, Category, Product

class CustomUserModelTest(TestCase):
    def test_custom_user_creation(self):
        user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.assertEqual(user.username, 'testuser')

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Test Category', slug='test-category')
        self.assertEqual(category.name, 'Test Category')

class ProductModelTest(TestCase):
    def test_product_creation(self):
        category = Category.objects.create(name='Test Category', slug='test-category')
        product = Product.objects.create(category=category, name='Test Product', description='Test description', price=10.0, stock=100)
        self.assertEqual(product.name, 'Test Product')

class CategoryListViewTest(TestCase):
    def test_category_list_view(self):
        category = Category.objects.create(name='Test Category', slug='test-category')
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['categories'], [category])

