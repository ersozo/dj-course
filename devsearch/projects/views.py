from django.shortcuts import render
from django.http import HttpResponse

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
    msg = "projects page"
    number = 10
    context = {"message": msg, "number": number, "projects": project_list}
    return render(
        request=request, template_name="projects/projects.html", context=context
    )


def project(request, pk):
    msg = "single project page"
    projectObj = None
    for i in project_list:
        if i["id"] == pk:
            projectObj = i
            break
    context = {"message": msg, "project": projectObj}
    return render(request, "projects/single-project.html", context)
