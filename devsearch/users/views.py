from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm


# Create your views here.
def login_user(request):
    page = "login"
    if request.user.is_authenticated:  # checks if user is authenticated
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error(request, "Username or password is incorrect")

    context = {"page": page}

    return render(request, template_name="users/login_register.html", context=context)


def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect("login")


def register_user(request):
    page = "register"
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created!")

            login(request, user)
            return redirect("profiles")

        else:
            messages.error(request, "An error has occurred during registration")
    context = {"page": page, "form": form}
    return render(request, template_name="users/login_register.html", context=context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, template_name="users/profiles.html", context=context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")

    context = {
        "profile": profile,
        "top_skills": top_skills,
        "other_skills": other_skills,
    }
    return render(request, template_name="users/user-profile.html", context=context)
