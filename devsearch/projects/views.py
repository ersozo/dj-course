from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

project_list = [
    {
        "id": "1",
        "title": "E-commerce website",
        "description": "Fully functional e-commerce website",
    },
    {
        "id": "2",
        "title": "Portfolio website",
        "description": "This was a project where I built out my portfolio",
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "Awesome open source project I am still working",
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(
        request=request, template_name="projects/projects.html", context=context
    )


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {"projectObj": projectObj}

    return render(request, "projects/single-project.html", context)
