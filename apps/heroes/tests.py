from django.test import TestCase
from apps.heroes.serializers import HeroesSerializer, Heroes, HeroesCategories, HeroesCategorySerializer
# Create your tests here.


class HeroesSerializerTestCase(TestCase):
    def test_heroes_serializer(self):
        heroes = Heroes.object.create(name='Ван Ван', role="Mage", complexity=56, description='SuperArcher')
        srz = HeroesSerializer(heroes, many=False)
        exepted_data = {
            'id': heroes.id,
            'name': 'Наушники',
            'role': 'Mage',
            'complexity': 56,
            'description': "SuperArcher"
        }
        self.assertEqual(srz.data, exepted_data)


class HeroesCategorySerializerTestCase(TestCase):

    def test_heroes_category_serializer(self):
        category = HeroesCategories.object.create(title="Mage")
        srz = HeroesCategorySerializer(category, many=False)
        expected_data = {
            'id': category.id,
            'name': 'Mage',
            'heroes': [],
        }
        result = srz.data
        self.assertEqual(result, expected_data)

