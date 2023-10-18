from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_now, logout as logout_now
from .models import *
from django.contrib import messages


def home_route(request):
    context = {}
    return render(request, "app/home_route.html", context)


def contact_route(request):
    context = {}
    return render(request, "app/contact_route.html", context)


def faq_route(request):
    context = {}
    return render(request, "app/faq_route.html", context)
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
            if username=="admin" or username=="admin_user":
                return redirect("app:admin-dashboard-route")
            elif user.account_type == "1":
                return redirect("app:staff-dashboard-route")
            else:
                return redirect("app:home-route")
        else:
            messages.error(request, "Invalid Username/Password")
            return redirect(request.META.get("HTTP_REFERER"))
    context = {}
    return render(request, "app/login_route.html", context)



def logout_route(request):
    logout_now(request)
    return redirect("/")

