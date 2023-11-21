# seed_data.py

from django.core.management.base import BaseCommand
from faker import Faker
import json
from mydukaapp.models import Category, Product, UserProfile, Review, ProductVariation, Cart, Order, OrderItem, Payment
from django.core import serializers

class Command(BaseCommand):
    help = 'Generate seed data using Faker and save it to a fixture file'

    def handle(self, *args, **options):

        fake = Faker()

        # Generate fake data for Category and Product models
        categories = [
            {
                "model": "mydukaapp.category",
                "pk": i,
                "fields": {
                    "name": fake.word(),
                    "slug": fake.slug(),
                }
            }
            for i in range(1, 6)  # Generate 5 categories
        ]

        products = [
            {
                "model": "mydukaapp.product",
                "pk": i,
                "fields": {
                    "category": fake.random_int(min=1, max=5),  # Assign a random category
                    "name": fake.word(),
                    "description": fake.sentence(),
                    "price": fake.random_element(elements=("999.99", "799.99", "599.99")),
                    "image": f"products/{fake.word()}.jpg",
                    "stock": fake.random_int(min=5, max=50),
                }
            }
            for i in range(1, 11)  # Generate 10 products
        ]

        # Combine category and product data
        seed_data = categories + products

        # # Save the seed data to a JSON file
        # with open('seed_data.json', 'w') as f:
        #     json.dump(seed_data, f, indent=4)
# from django.core.management.base import BaseCommand
# from faker import Faker
# import json

# from mydukaapp.models import Category, Product, UserProfile, Review, ProductVariation, Cart, Order, OrderItem, Payment
# from django.core import serializers

# class Command(BaseCommand):
#     help = 'Generate seed data using Faker and save it to a fixture file'

#     def handle(self, *args, **options):
#         fake = Faker()

#         # Generate data using Faker and save it to Django models
#         categories = [Category(name=fake.word()) for _ in range(5)]
#         Category.objects.bulk_create(categories)

#         products = [Product(category=fake.random_element(categories),
#                             name=fake.word(),
#                             description=fake.text(),
#                             price=fake.random_int(1, 100),
#                             image=fake.image_url(),
#                             stock=fake.random_int(1, 100)) for _ in range(20)]
#         Product.objects.bulk_create(products)

#         # ... Add more data generation for other models ...

        # Serialize the data to JSON and save it to a fixture file
        data = serializers.serialize("json", Category.objects.all()) + serializers.serialize("json", Product.objects.all())

        with open('seed_data.json', 'w') as json_file:
            json_file.write(data)

        self.stdout.write(self.style.SUCCESS('Successfully generated and saved seed data to seed_data.json'))
