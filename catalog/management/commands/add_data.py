from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = [
            {
                "category_name": "Фрукты",
                "descriptions_category": "Растут на деревьях",
                "id": 1

            },
            {
                "category_name": "Овощи",
                "descriptions_category": "Растут на кустах и в земле",
                "id": 2
            },
            {
                "category_name": "Ягоды",
                "descriptions_category": "Где только не растут",
                "id": 3
            }
        ]

        products = [
            {
                "product_name": "Яблоко",
                "descriptions": "Зеленое",
                "image_preview": "",
                "category": 1,
                "price": 20,
                "date_created": "2023-01-19T17:49:00Z",
                "date_of_change": "2023-01-19T17:49:03Z",
                "cat_fk": "Фрукты",
                "id": 1

            },
            {
                "product_name": "бананы",
                "descriptions": "обычный банан",
                "image_preview": "",
                "category": 1,
                "price": 23,
                "date_created": "2023-01-19T17:49:48Z",
                "date_of_change": "2023-01-19T17:49:50Z",
                "cat_fk": "Фрукты",
                "id": 2
            },
            {
                "product_name": "свёкла",
                "descriptions": "не сахарная",
                "image_preview": "",
                "category": 2,
                "price": 12,
                "date_created": "2023-01-19T17:50:59Z",
                "date_of_change": "2023-01-19T17:51:00Z",
                "cat_fk": "Овощи",
                "id": 3
            },
            {
                    "product_name": "голубика",
                    "descriptions": "дорогая",
                    "image_preview": "",
                    "category": 3,
                    "price": 80,
                    "date_created": "2023-01-19T17:52:06Z",
                    "date_of_change": "2023-01-19T17:52:07Z",
                    "cat_fk": "Ягоды",
                "id": 4
                }
        ]

        categories_list = []
        products_list = []
        Product.objects.all().delete()
        Category.objects.all().delete()


        for category in categories:
            categories_list.append(Category(**category))

        Category.objects.bulk_create(categories_list)


        for product in products:
            cat_item = Category.objects.get(category_name=product['cat_fk'])
            product['cat_fk'] = cat_item
            products_list.append(Product(**product))

        Product.objects.bulk_create(products_list)