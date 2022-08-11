from django.test import TestCase
from apps.heroes.serializers import HeroSerializer, Hero, HeroCategories, HeroCategorySerializer
# Create your tests here.


class HeroSerializerTestCase(TestCase):
    def test_hero_serializer(self):
        hero = Hero.object.create(name='Ван Ван', role="Mage", complexity=56, description='SuperArcher')
        srz = HeroSerializer(hero, many=False)
        expected_data = {
            'id': hero.id,
            'name': 'Ван Ван',
            'role': 'Mage',
            'complexity': 56,
            'description': "SuperArcher"
        }
        self.assertEqual(srz.data, expected_data)


class HeroCategorySerializerTestCase(TestCase):

    def test_hero_category_serializer(self):
        category = HeroCategories.object.create(title="Mage")
        srz = HeroCategorySerializer(category, many=False)
        expected_data = {
            'id': category.id,
            'name': 'Mage',
            'hero': [],
        }
        result = srz.data
        self.assertEqual(result, expected_data)

