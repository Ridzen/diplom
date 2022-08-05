from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class PostCategories(models.Model):
    """Модель новостей про героев(категории)"""

    key_news = models.CharField(max_length=255, unique=False)

    class Meta:
        verbose_name_plural = 'Категория новостей'
        verbose_name = 'Категория новости'

    def __str__(self):
        return self.key_news


class Post(models.Model):
    images = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    text = RichTextUploadingField()
    tag = models.CharField(max_length=50, null=True, blank=True)
    in_archive = models.BooleanField(default=False)

    class Meta():
        db_table = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title




