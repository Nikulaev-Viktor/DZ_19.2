from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Модель категории"""
    title = models.CharField(max_length=200, verbose_name='Категория', help_text='Введите категорию', )
    description = models.TextField(verbose_name='Описание категории',
                                   help_text='Введите описание категории', **NULLABLE, )

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']


class Product(models.Model):
    """Модель продукта"""
    title = models.CharField(max_lenght=200, verbose_name='Название товара',
                             help_text="Введите наименование продукта", )
    description = models.TextField(verbose_name='Описание продукта', help_text="Введите описание продукта", )
    image = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)',
                              help_text='Вставьте изображение продукта', **NULLABLE, )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 verbose_name='Категория', help_text= 'Введите категорию', **NULLABLE,
                                 related_name='products', )
    price = models.IntegerField(verbose_name='Цена, за покупку')
    created_at = models.DateTimeField(verbose_name='Дата создания записи в БД', **NULLABLE)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения записи в БД')

    def __str__(self):
        return f'{self.title} {self.description} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['title']
