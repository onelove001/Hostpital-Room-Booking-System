from django.shortcuts import *
from .models import *


# Admin Routes

def admin_dashboard_route(request):
    gym_profiles = Gym.objects.all()
    classes = Class.objects.all()
    memberships = Membership.objects.all()
    coaches = Coach.objects.all()
    context = {"gym_profiles":gym_profiles, "classes":classes, "memberships":memberships, "coaches":coaches}
    return render(request, "admin/admin_board_route.html", context)


def create_class_route(request):
    coaches = Coach.objects.all()
    if request.method == "POST":
        name = request.POST.get("class_name")
        description = request.POST.get("description")
        coach = request.POST.get("coach")
        coach_obj=Coach.objects.get(id = coach)
        classs = Class(coach=coach_obj, class_name=name, class_description=description)
        classs.save()
    context = {"coaches":coaches}
    return render(request, "admin/create_class_route.html", context)


def create_coach_route(request):
    if request.method == "POST":
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        address = request.POST.get("address")
        mobile = request.POST.get("mobile_number")
        coach = Coach(coach_firstname=firstname, coach_lastname=lastname, coach_address=address, coach_mobile=mobile)
        coach.save()
    context = {}
    return render(request, "admin/create_coach_route.html", context)


def create_membership_route(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        coaches = request.POST.get("coaches")
        membership = Membership(membership_name=name, maximum_coach=coaches, membership_description=description, membership_price=price)
        membership.save()
    context = {}
    return render(request, "admin/create_membership_route.html", context)


def approve_or_dissaprove_route(request, gym_id):
    gym = Gym.objects.get(id = gym_id)
    if gym.status:
        gym.status = False
    else:
        gym.status = True
    gym.save()
    return redirect(request.META.get("HTTP_REFERER"))