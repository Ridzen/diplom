from django.contrib import admin

from apps.heroes.models import HeroesCategories, Heroes, HeroesSkills


@admin.register(Heroes)
class AdminHeroes(admin.ModelAdmin):
    pass


@admin.register(HeroesCategories)
class AdminHeroesCategory(admin.ModelAdmin):
    pass


@admin.register(HeroesSkills)
class AdminSkills(admin.ModelAdmin):
    pass
