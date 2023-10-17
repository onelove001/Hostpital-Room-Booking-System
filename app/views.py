from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_now, logout as logout_now
from .models import *


def home_route(request):
    context = {}
    return render(request, "app/home_route.html", context)


def contact_route(request):
    context = {}
    return render(request, "app/contact_route.html", context)


def blog_route(request):
    context = {}
    return render(request, "app/blog_route.html", context)


def faq_route(request):
    context = {}
    return render(request, "app/faq_route.html", context)


def membership_route(request):
    memberships = Membership.objects.all()
    context = {"memberships":memberships}
    return render(request, "app/membership_route.html", context)
    

def class_route(request):
    classes = Class.objects.all()
    context = {"classes":classes}
    return render(request, "app/class_route.html", context)


def coach_route(request):
    coaches = Coach.objects.all()
    context = {"coaches":coaches}
    return render(request, "app/coach_route.html", context)


def login_route(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            login_now(request, user)
            if username=="admin":
                return redirect("app:admin-dashboard-route")
            return redirect("app:home-route")
    context = {}
    return render(request, "app/login_route.html", context)


def join_route(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        mobile = request.POST.get("mobile")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        patient = CustomUser.objects.create_user(account_type = 2, username = username, first_name = first_name, last_name = last_name,  password = password)
        patient.gender = gender
        patient.dateOfBirth = dob
        patient.phone_no = phone
        patient.save()
        return redirect("app:login-route")
    context = {}
    return render(request, "app/join_route.html", context)


def logout_route(request):
    logout_now(request)
    return redirect("app:login-route")


def my_gym_route(request):
    user = request.user
    classes = Class.objects.all()
    memberships = Membership.objects.all()
    if request.method == "POST":
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        member = request.POST.get("membership")
        classs = request.POST.get("class")
        schedule = request.POST.get("schedule")
        profile = Profile.objects.get(user_profile = user)
        profile.address_location = address
        profile.mobile_number = mobile
        profile.save()
        membership_obj = Membership.objects.get(id = member)
        class_obj = Class.objects.get(id = classs)
        gym = Gym(profile=profile, membership_id=membership_obj, class_id=class_obj, schedule=schedule)
        gym.save()
    gym_profiles = Gym.objects.filter(profile=request.user.profile)
    context = {"user":user, "classes":classes, "memberships":memberships, "gym_profiles":gym_profiles}
    return render(request, "app/my_gym_route.html", context)


