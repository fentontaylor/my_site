from django.shortcuts import render
from projects.models import Project, Technology


def project_index(request):
    projects = Project.objects.all()
    context = { 'projects': projects }
    return render(request, 'project_index.html', context)


def project_show(request, pk):
    project = Project.objects.get(pk=pk)
    tech_list = list(project.technologies.all())
    context = {
        'project': project,
        'tech_list': tech_list
    }
    return render(request, 'project_show.html', context)