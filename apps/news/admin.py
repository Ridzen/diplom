from django.contrib import admin
from apps.news.models import Post, PostCategories, NewsComment, CommentReply

# Register your models here.


@admin.register(Post)
class AdminHeroes(admin.ModelAdmin):
    pass


@admin.register(PostCategories)
class AdminHeroes(admin.ModelAdmin):
    pass


admin.site.register(NewsComment)
admin.site.register(CommentReply)
