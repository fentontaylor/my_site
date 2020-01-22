from django.test import TestCase
from projects.models import Project, Technology

class ProjectTest(TestCase):
    def setUp(self):
        Project.objects.create(
            title = 'MyProject',
            description = 'It does cool things',
            language = 'Python',
            # technologies = models.ManyToManyField('Technology', related_name='projects', blank=True, default='')
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