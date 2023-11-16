from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from backend.gallery.serializers import GallerySer

def create_pereval(self):
    """добавление перевала"""

    return Pereval_added.objects.create(user=self.user, beauty_title='test',\
                                  title='title-test', other_titles='other_title',\
                                  level=self.level, coord=self.coord, image=self.images)


class ApiModelTest(TestCase):
    """Тестирование моделей, создание перевалов"""

    def setUp(self):
        # Setup run before every test method.
        self.user = User.objects.create(first_name='first-test',
                                         last_name='last-test',
                                         middle_name='middle-test',
                                         email='test@example.com',
                                         phone='+79306567898')
        self.level = Level.objects.create(winter='1A')
        self.coord = Coords.objects.create(latitude='2', longitude='5', height='0')
        self.image = GallerySer.objects.create(title='Null', image='null')

    def test_setUpTestData(self):
        new = create_pereval(self)
        self.assertEqual(new.beauty_title, 'test')


class PersonViewSetTests(APITestCase):

    def test_list_pereval(self):
        """Тест для всех перевалов в списке"""

        url = 'http://127.0.0.1:8000%s' % reverse('transition-list')

        response = self.client.get(url, format='json')
        json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(json), 4)





