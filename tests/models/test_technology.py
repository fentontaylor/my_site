from django.test import TestCase
from projects.models import Technology

class TechnologyTest(TestCase):
    def setUp(self):
        Technology.objects.create(name='Flask')
        Technology.objects.create(name='PostgreSQL')

    
    def test_attribute(self):
        flask = Technology.objects.get(name='Flask')
        pg = Technology.objects.get(name='PostgreSQL')

        self.assertEqual(flask.name, 'Flask')
        self.assertEqual(pg.name, 'PostgreSQL')