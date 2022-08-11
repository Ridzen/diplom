from django.test import TestCase
from apps.heroes.serializers import HeroSerializer, Hero, HeroCategories, HeroCategorySerializer
# Create your tests here.


class HeroSerializerTestCase(TestCase):
    def test_heroes_serializer(self):
        heroes = Hero.object.create(name='Ван Ван', role="Mage", complexity=56, description='SuperArcher')
        srz = HeroSerializer(heroes, many=False)
        exepted_data = {
            'id': heroes.id,
            'name': 'Наушники',
            'role': 'Mage',
            'complexity': 56,
            'description': "SuperArcher"
        }
        self.assertEqual(srz.data, exepted_data)


class HeroCategorySerializerTestCase(TestCase):

    def test_heroes_category_serializer(self):
        category = HeroCategories.object.create(title="Mage")
        srz = HeroCategorySerializer(category, many=False)
        expected_data = {
            'id': category.id,
            'name': 'Mage',
            'heroes': [],
        }
        result = srz.data
        self.assertEqual(result, expected_data)

