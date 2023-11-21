from django.core.management.base import BaseCommand
from faker import Faker
import json
from django.core import serializers
from django.utils.text import slugify  # Import slugify

from mydukaapp.models import Category, Product

class Command(BaseCommand):
    help = 'Generate seed data using Faker and save it to a fixture file'

    def handle(self, *args, **options):
        fake = Faker()

        # Generate data using Faker and save it to Django models
        categories = []
        for _ in range(5):
            name = fake.word()
            slug = slugify(name)  # Generate a unique slug based on the name
            categories.append(Category(name=name, slug=slug))
        Category.objects.bulk_create(categories)

        products = [Product(category=fake.random_element(categories),
                            name=fake.word(),
                            description=fake.text(),
                            price=fake.random_int(1, 100),
                            image=fake.image_url(),
                            stock=fake.random_int(1, 100)) for _ in range(20)]
        Product.objects.bulk_create(products)

        # Serialize the data to JSON and save it to a fixture file
        data = serializers.serialize("json", Category.objects.all()) + serializers.serialize("json", Product.objects.all())

        with open('seed_data.json', 'w') as json_file:
            json_file.write(data)

        self.stdout.write(self.style.SUCCESS('Successfully generated and saved seed data to seed_data.json'))
