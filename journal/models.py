from django.db import models
from django.urls import reverse
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Описание статьи')
    date = models.DateField(default=timezone.now, verbose_name='Время создания')
    categ = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
