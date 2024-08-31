import json

from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog.json', encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('catalog.json', encoding="utf-8") as file:
            return json.load(file)

    def handle(self, *args, **options):
        Category.objects.all().delete()  # Удаляем все категории
        Product.objects.all().delete()  # Удаляем все продукты
        category_for_create = []  # Создайте списки для хранения объектов
        product_for_create = []  # Создайте списки для хранения объектов

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'], name=category["fields"]["title"],
                         description=category["fields"]["description"])
            )
        Category.objects.bulk_create(category_for_create)  # Создаем объекты в базе с помощью метода bulk_create()

        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product['pk'], title=product["fields"]["title"],
                        description=product["fields"]["description"],
                        image=product["fields"]["image"],
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        price=product["fields"]["price"],
                        created_at=product["fields"]["created_at"],
                        updated_at=product["fields"]["updated_at"])
            )

            Product.objects.bulk_create(product_for_create)  # Создаем объекты в базе с помощью метода bulk_create()

