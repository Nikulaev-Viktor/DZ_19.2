from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """Модель категории"""

    title = models.CharField(
        max_length=200,
        verbose_name="Категория",
        help_text="Введите категорию",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["title"]


class Product(models.Model):
    """Модель продукта"""

    title = models.CharField(
        max_length=200,
        verbose_name="Название товара",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Изображение(превью)",
        help_text="Вставьте изображение продукта",
        **NULLABLE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        **NULLABLE,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена, за покупку")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания записи в БД", **NULLABLE
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения записи в БД"
    )
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE, related_name='authors')

    def __str__(self):
        return f"{self.title} {self.description} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["title", "author"]
        permissions = [
            ('cancel_publication', 'может отменять публикацию'),
            ('can_change_description', 'может менять описание любого продукта'),
            ('can_change_category', 'может менять категорию любого продукта')
        ]


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.CASCADE,
        verbose_name="продукт",
        **NULLABLE,
    )
    version_number = models.PositiveIntegerField(
        verbose_name="Номер версии", help_text="номер версии продукта"
    )
    version_name = models.CharField(
        max_length=150,
        verbose_name="Наименование версии",
        help_text="Наименование версии продукта",
    )
    version_active = models.BooleanField(default=False, verbose_name="Активная версия")

    def __str__(self):
        return f'{self.version_name}'

    class Meta:
        verbose_name = 'Версия продукта'
        verbose_name_plural = 'Версии продукта'
        ordering = ('version_name', 'version_number')

