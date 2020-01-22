from projects.views import project_index


def root_index(request):
    return project_index(request)