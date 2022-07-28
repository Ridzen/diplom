from rest_framework import serializers

from apps.heroes.models import HeroesCategories, HeroesSkills, Heroes


class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        fields = ('__all__')

    def create(self, validated_data):
        return Heroes.objects.create(**validated_data)


class HeroesCategorySerializer(serializers.ModelSerializer):
    heroes = HeroesSerializer(many=True)

    class Meta:
        model = HeroesCategories
        fields = "__all__"


class HeroesSkillsSerializer(serializers.ModelSerializer):
    heroes = HeroesSerializer(many=True, read_only=True)

    class Meta:
        model = HeroesSkills
        fields = "__all__"
