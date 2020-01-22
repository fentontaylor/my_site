from django.test import TestCase
from projects.models import Technology, Project

class TechnologyTest(TestCase):
    def setUp(self):
        Technology.objects.create(name='Flask')
        Technology.objects.create(name='PostgreSQL')

    
    def test_attribute(self):
        flask = Technology.objects.get(name='Flask')
        pg = Technology.objects.get(name='PostgreSQL')

        self.assertEqual(flask.name, 'Flask')
        self.assertEqual(pg.name, 'PostgreSQL')


    def test_can_belong_to_many_projects(self):
        tech = Technology.objects.get(name='PostgreSQL')
        p1 = Project.objects.create(title='Rails Project', description='Its Rails', language='Ruby')
        p2 = Project.objects.create(title='Django Project', description='Its Python', language='Python')
        tech.projects.add(p1, p2)
        proj_list = list(tech.projects.all())
        self.assertListEqual(proj_list, [p1, p2])