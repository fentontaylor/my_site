from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=30)

    def __repr__(self):
        return f"<Technology: name='{self.name}'>"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=20)
    technologies = models.ManyToManyField('Technology', related_name='projects', blank=True)
    image = models.FilePathField(path='/img')
    github = models.URLField(max_length=200, blank=True, null=True)
    production = models.URLField(max_length=200, blank=True, null=True)

    def __repr__(self):
        desc = f'{self.description[0:7]}...'
        return f"<Project: title='{self.title}', " \
                         f"description='{desc}', " \
                         f"language='{self.language}', " \
                         f"image='{self.image}', " \
                         f"github='{self.github}', " \
                         f"production='{self.production}'>"

    def __str__(self):
        return self.title