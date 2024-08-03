from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.CharField(
        max_length=100,
        choices=[
            ('books', 'Книги'), ('clothes', 'Одежда'),
            ('Food', 'Еда')
            ], verbose_name='Категория')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name='Картинка')

    def __repr__(self):
        return self.name