from django.db import models
from pytils.translit import slugify


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):

    category_name = models.CharField(max_length=200, verbose_name='Категория')
    descriptions_category = models.CharField(max_length=300, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):

    product_name = models.CharField(max_length=200, verbose_name='Название')
    descriptions = models.CharField(max_length=300, verbose_name='Описание')
    image_preview = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение')
    category = models.IntegerField(verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_created = models.DateTimeField(verbose_name='Дата создания')
    date_of_change = models.DateTimeField(verbose_name='Дата изменения')

    cat_fk = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f'{self.id} {self.product_name} {self.price} {self.category}'


class Blog(models.Model):

    STATUSES = (
        ('active', 'активно'),
        ('moderation', 'модерация')
    )
    STATUS_ACTIVE = 'active'
    STATUS_MODERATION = 'moderation'

    header = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, null=True, blank=True, verbose_name='URL')
    content = models.CharField(max_length=600, verbose_name='содержимое')
    image_preview = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение')
    date_created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    publication_status = models.CharField(max_length=15, default=STATUS_MODERATION, choices=STATUSES, verbose_name='признак публикации')
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def save(self, *args, **kwargs):
        value = self.header
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def __str__(self):
        return f'{self.header} {self.content}'


class Version(models.Model):
    STATUSES = (
        ('active', 'активная'),
        ('outdated', 'устаревшая')
    )
    STATUS_ACTIVE = 'active'
    STATUS_OUTDATED = 'outdated'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер')
    version_name = models.CharField(max_length=35, verbose_name='Название')
    sign = models.CharField(max_length=15, default=STATUS_ACTIVE, choices=STATUSES, verbose_name='Признак')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.version_name}'



