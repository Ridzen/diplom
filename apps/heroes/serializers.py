from rest_framework import serializers

from apps.heroes.models import (
    HeroesCategories, HeroesSkills, Heroes
                                )


class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        fields = (
            'id', 'images', 'name', 'role', 'complexity', 'description', 'skill',
        )

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def create(self, validated_data):
        return Heroes.objects.create(**validated_data)


class HeroesCategorySerializer(serializers.ModelSerializer):
    heroes = HeroesSerializer(many=True)

    class Meta:
        model = HeroesCategories
        fields = ('key_role', 'heroes')


class HeroesSkillsSerializer(serializers.ModelSerializer):
    heroes = HeroesSerializer(many=True)

    class Meta:
        model = HeroesSkills
        fields = (
            "first_skill", 'image_first', 'second_skill', 'image_second', 'third_skill', "image_third", 'passive_skill',
            'heroes', 'imagine_passive',
        )

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

