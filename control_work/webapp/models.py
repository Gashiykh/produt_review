from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.CharField(
        max_length=100,
        choices=[
            ('books', 'Книги'), ('clothes', 'Одежда'),
            ('Food', 'Еда')
        ],
        verbose_name='Категория'
    )
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name='Картинка')

    def __repr__(self):
        return self.name
    

class Review(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='reviews', verbose_name='Товар')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    feedback = models.TextField(max_length=1000, verbose_name='Текст отзыва')
    rating = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        choices=[
            (1, '1'),
            (2, '2'), 
            (3, '3'), 
            (4, '4'), 
            (5, '5'),
        ]
    )

    def __repr__(self) -> str:
        return f'Отзыв от {self.author.username} для {self.product.name}'