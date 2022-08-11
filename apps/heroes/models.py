from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class HeroesCategories(models.Model):
    """
    Модель ролей героев
    """

    key_role = models.CharField(max_length=255, unique=False)

    class Meta:
        verbose_name_plural = 'Категория ролей'
        verbose_name = 'Категория роли'

    def __str__(self):
        return self.key_role


class HeroesSkills(models.Model):
    """
    Моделька для скиллов
    """
    first_skill = RichTextUploadingField()
    image_first = models.ImageField(null=True, blank=True)
    second_skill = RichTextUploadingField()
    image_second = models.ImageField(null=True, blank=True)
    third_skill = RichTextUploadingField()
    image_third = models.ImageField(null=True, blank=True)
    passive_skill = RichTextUploadingField()
    image_passive = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = 'skills_db'
        verbose_name_plural = 'Скиллы'
        verbose_name = "Скилл"

    def __str__(self):
        return self.first_skill


class Heroes(models.Model):
    """
    Моделька для героев
    """

    images = models.ImageField()
    name = models.CharField(max_length=150)
    role = models.ForeignKey(
        to=HeroesCategories, on_delete=models.CASCADE, related_name='hero',
                             default=None, null=True
    )
    complexity = models.IntegerField(default=0, null=True)
    description = models.TextField()
    skill = models.ForeignKey(
        HeroesSkills, on_delete=models.CASCADE, related_name='hero',
                              default=None, null=True
    )

    class Meta:
        db_table = 'heroes_db'
        verbose_name_plural = 'Герои'
        verbose_name = "Герой"

    def __str__(self):
        return self.name
