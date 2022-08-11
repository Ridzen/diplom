from django.contrib import admin

from apps.heroes.models import (
    HeroCategories, Hero, HeroSkills
)


@admin.register(Hero)
class AdminHero(admin.ModelAdmin):
    pass


@admin.register(HeroCategories)
class AdminHeroCategory(admin.ModelAdmin):
    pass


@admin.register(HeroSkills)
class AdminSkills(admin.ModelAdmin):
    pass
