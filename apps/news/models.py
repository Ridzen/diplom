from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class PostCategories(models.Model):
    """Модель новостей про героев(категории)"""

    key_news = models.CharField(
        max_length=255, unique=False
    )

    class Meta:
        verbose_name_plural = 'Категория новостей'
        verbose_name = 'Категория новости'

    def __str__(self):
        return self.key_news


class Post(models.Model):
    images = models.ImageField(
        null=True, blank=True
    )
    title = models.CharField(
        max_length=255
                             )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    text = RichTextUploadingField()
    tag = models.CharField(
        max_length=50, null=True, blank=True
    )
    in_archive = models.BooleanField(
        default=False
    )

    class Meta():
        db_table = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


User = get_user_model()


class NewsComment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор', related_name='user_comments'
    )
    text = models.TextField(
        verbose_name='Комментарий'
    )
    created_data = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления'
    )
    likes = models.ManyToManyField(
        User, related_name='liked_comments', blank=True,
        verbose_name='Пользователи, которым нравится комментарий'
    )
    total_likes = models.PositiveIntegerField(
        default=0, verbose_name='Кол-во лайков', db_index=True,
    )


class CommentReply(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор'
    )
    comment = models.ForeignKey(
        NewsComment, on_delete=models.CASCADE, verbose_name='Коммент', related_name='replies'
    )
    text = models.TextField(
        verbose_name='Ответ на комментарий'
    )
    likes = models.ManyToManyField(
        User, related_name='liked_replies', blank=True,
        verbose_name='Пользователи, которым нравится ответ на комментарий'
    )
    total_likes = models.PositiveIntegerField(
        default=0, verbose_name='Кол-во лайков', db_index=True,
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        if self.author.username:
            return f'Автор: {self.author.username}, Ответ на комментарий: {self.text}'
        return f'Автор: {self.author.email}, Ответ на комментарий: {self.text}'

    class Meta:
        verbose_name = 'Ответ на комментарий'
        verbose_name_plural = 'Ответы на комментарии'



