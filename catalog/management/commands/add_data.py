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
                    "descriptions": "плоды дерева яблони, которые употребляются в пищу в свежем, сухом или консервированном виде, применяются в различных блюдах в качестве ингредиентов или используются в виде основы для получения соков.",
                    "image_preview": "product/zelyonie_yabloki_1.jpg",
                    "category": "Фрукты",
                    "price": 20,
                    "date_created": "2023-01-19T17:49:00Z",
                    "date_of_change": "2023-01-19T17:49:03Z"
                },

            {
                    "product_name": "бананы",
                    "descriptions": "В конце XX века ученые доказали, что в бананах содержатся вещества, близкие по структуре к так называемому гормону счастья серотонину. Это вещество вызывает у человека прилив сил и ощущение радости. Давайте же есть бананы и радоваться! Банан, достигающий высоты 6–7,5 м, часто по ошибке называют дер",
                    "image_preview": "product/banan.jpg",
                    "category": "Фрукты",
                    "price": 23,
                    "date_created": "2023-01-19T17:49:48Z",
                    "date_of_change": "2023-01-19T17:49:50Z"
                },
            {
                    "product_name": "помидор",
                    "descriptions": "однолетнее или многолетнее травянистое растение, вид рода Паслён (Solanum) семейства Паслёновые (Solanaceae). Возделывается как овощная культура; выращивается ради съедобных плодов — сочных многогнёздных ягод различной формы и окраски, также называемых томатами или помидорами.",
                    "image_preview": "product/1625169739_1-kartinkin-com-p-pomidor-yeda-krasivo-foto-1.jpg",
                    "category": "Овощи",
                    "price": 15,
                    "date_created": "2023-01-19T17:50:19Z",
                    "date_of_change": "2023-01-19T17:50:21Z"
            },
            {
                    "product_name": "свёкла",
                    "descriptions": "овощ-корнеплод, один из самых традиционных продуктов русской кухни. На Западе многие шефы считают ее символом русской кухни. Впрочем, знают свёклу и во многих других странах. Свёкла очень полезна, причём сохраняет свои полезные качества в любом виде, что бы вы с ней ни делали - жарили, парили, варил",
                    "image_preview": "product/svekla.jpg",
                    "category": "Овощи",
                    "price": 12,
                    "date_created": "2023-01-19T17:50:59Z",
                    "date_of_change": "2023-01-19T17:51:00Z"
            },
            {
                    "product_name": "малина",
                    "descriptions": "плодовый листопадный полукустарник, относящийся к виду рода Рубус, семейства Розовые. Из самых лучших сортов можно делать травяные настойки и чаи, использовать сочные и ароматные плоды малины для потребления в пищу.  Благодаря своей неприхотливости малина распространилась по всему миру.",
                    "image_preview": "product/Raspberry_Closeup_436975.jpg",
                    "category": "Ягоды",
                    "price": 50,
                    "date_created": "2023-01-19T17:51:30Z",
                    "date_of_change": "2023-01-19T17:51:32Z"

            },
            {
                    "product_name": "голубика",
                    "descriptions": "Голубика является кустарником. В высоту он обычно около 30 сантиметров. Растение сильно разветвлено. Каждый стебель устремлен вверх и имеет круглое сечение. Цвет у стволов бурый. ... Где растет голубика, там почвы болотистые, кислые. На бедных почвах, к примеру, песчаных, ягода встречается, но мелка",
                    "image_preview": "product/gol.jpeg",
                    "category": "Ягоды",
                    "price": 80,
                    "date_created": "2023-01-19T17:52:06Z",
                    "date_of_change": "2023-01-19T17:52:07Z"
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
            cat_item = Category.objects.get(category_name=product['category'])
            product['category'] = cat_item
            products_list.append(Product(**product))

        Product.objects.bulk_create(products_list)