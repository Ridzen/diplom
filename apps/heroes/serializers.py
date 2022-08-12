from rest_framework import serializers

from apps.heroes.models import (
    HeroCategories, HeroSkills, Hero
                                )


class HeroSkillsNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSkills
        fields = ('id', "first_skill", 'image_first', 'second_skill', 'image_second',
            'third_skill', "image_third", 'passive_skill', 'image_passive',)


class HeroSerializer(serializers.ModelSerializer):

    skill = HeroSkillsNestedSerializer(many=False)
    class Meta:
        model = Hero
        fields = (
            'id', 'images', 'name', 'role', 'complexity', 'description', 'skill',
        )

    def get_image(self, obj):
        try:
            image = obj.images.url
        except AttributeError:
            image = None
        return image

    def create(self, validated_data):
        return Hero.objects.create(**validated_data)


class HeroCategorySerializer(serializers.ModelSerializer):
    hero = HeroSerializer(many=True)

    class Meta:
        model = HeroCategories
        fields = ('key_role', 'hero')


