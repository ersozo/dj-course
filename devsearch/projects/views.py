from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(
        request=request, template_name="projects/projects.html", context=context
    )


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {"project": projectObj}

    return render(request, "projects/single_project.html", context)


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("account")
    context = {"object": project}
    return render(request, "delete_template.html", context)
