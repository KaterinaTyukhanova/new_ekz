from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Tovar(models.Model):
    name = models.CharField(blank=False, verbose_name='Название товара', max_length=50)
    information = models.TextField(blank=False, verbose_name='Информация о товаре (описание)', max_length=250)
    tovar_photo = models.ImageField(upload_to='images/', verbose_name='Изображение товара', blank=True)
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])

class User(AbstractUser):
    photo = models.ImageField(upload_to='images/', verbose_name='Фото пользователя', blank=True)


class Zakaz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Tovar, on_delete=models.CASCADE)