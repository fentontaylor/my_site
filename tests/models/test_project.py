from django.test import TestCase
from projects.models import Project, Technology

class ProjectTest(TestCase):
    def setUp(self):
        Project.objects.create(
            title = 'MyProject',
            description = 'It does cool things',
            language = 'Python',
            image = 'sample.png',
            github = 'github.com/me/my_project',
            production = 'my_project.herokuapp.com',
        )

    def test_attributes(self):
        proj = Project.objects.get(title='MyProject')

        self.assertEqual(proj.title, 'MyProject')
        self.assertEqual(proj.description, 'It does cool things')
        self.assertEqual(proj.language, 'Python')
        self.assertEqual(proj.image, 'sample.png')
        self.assertEqual(proj.github, 'github.com/me/my_project')
        self.assertEqual(proj.production, 'my_project.herokuapp.com')

    
    def test_it_can_have_many_technologies(self):
        proj = Project.objects.get(title='MyProject')
        t1 = Technology.objects.create(name='Django')
        t2 = Technology.objects.create(name='PostgreSQL')
        proj.technologies.add(t1, t2)
        tech_list = list(proj.technologies.all())
        self.assertListEqual(tech_list, [t1, t2])
