from django.test import TestCase
from apps.news.serializers import Post, PostCategories, PostSerializer, PostCategorySerializer


class PostSerializerTestCase(TestCase):
    def test_heroes_serializer(self):
        post = Post.object.create(name='Super 1.167.123', text="This update msg", tag='updates')
        srz = PostSerializer(post, many=False)
        expected_data = {
            'id': post.id,
            'title': 'Super 1.167.123',
            'text': 'This update msg',
            'tag': 'updates',
        }
        self.assertEqual(srz.data, expected_data)


class PostCategorySerializerTestCase(TestCase):

    def test_heroes_category_serializer(self):
        category = PostCategories.object.create(key_news="Updates")
        srz = PostCategorySerializer(category, many=False)
        expected_data = {
            'id': category.id,
            'key_news': 'Updates',
            'post': [],
        }
        result = srz.data
        self.assertEqual(result, expected_data)