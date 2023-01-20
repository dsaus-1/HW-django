from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):

    category_name = models.CharField(max_length=200, verbose_name='Категория')
    descriptions_category = models.CharField(max_length=300, verbose_name='Описание')

    def __str__(self):
        return f'{self.id} {self.category_name}'


class Product(models.Model):

    product_name = models.CharField(max_length=200, verbose_name='Название')
    descriptions = models.CharField(max_length=300, verbose_name='Описание')
    image_preview = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение')
    category = models.IntegerField(verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_created = models.DateTimeField(verbose_name='Дата создания')
    date_of_change = models.DateTimeField(verbose_name='Дата изменения')

    cat_fk = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} {self.product_name} {self.price} {self.category}'




