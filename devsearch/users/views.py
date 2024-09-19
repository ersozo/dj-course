from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.contrib.auth.models import User


from .models import Profile


# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            print("Username or password is incorrect")

    return render(request, template_name="users/login_register.html")


def logout_user(request):
    logout(request)
    return redirect("login")


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
