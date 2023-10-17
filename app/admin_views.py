from django.shortcuts import *
from .models import *
from django.contrib import messages


# Admin Routes
def admin_dashboard_route(request):
    context = {}
    return render(request, "admin/admin_board_route.html", context)


def create_staff(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        phone  = request.POST.get("phone")
        password  = request.POST.get("password")
        staff = CustomUser.objects.create_user(account_type=1, first_name = first_name, last_name = last_name, username = username)
        staff.staff.phone_no = phone
        staff.save()
        messages.success(request, "Staff Created!")
        return redirect(request.META.get("HTTP_REFERER"))

    context = {}
    return render(request, "admin/create_staff.html", context)


def manage_staffs(request):
    staffs = CustomUser.objects.filter(account_type=1)
    context = {"staffs":staffs}
    return render(request, "admin/manage_staffs.html", context)


def update_staff(request, staff_id):
    staff = CustomUser.objects.get(id = staff_id)
    if request.method=="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_no = request.POST.get("phone")
        staff.first_name = first_name
        staff.last_name = last_name
        staff_obj = Staff.objects.get(user_profile=staff)
        staff_obj.phone_no = phone_no
        staff.save()
        staff_obj.save()
        messages.success(request, "Staff Updated!")
        return redirect(request.META.get("HTTP_REFERER"))

    context = {"staff":staff}
    return render(request, "admin/update_staff.html", context)


def delete_staff(request, staff_id):
    staff = CustomUser.objects.get(id = staff_id)
    staff.delete()
    return redirect("app:manage-staffs")


def create_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room_number")
        beds = request.POST.get("beds")
        room = Room(room_number = room_number, beds = beds, status = False)
        room.save()
        messages.success(request, "Room Created!")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {}
    return render(request, "admin/create_room.html", context)


def manage_rooms(request):
    rooms = Room.objects.all()
    context = {"rooms":rooms}
    return render(request, "admin/manage_rooms.html", context)


def update_room(request, room_id):
    room = Room.objects.get(id = room_id)
    if request.method == "POST":
        room_n = request.POST.get("room_number")
        beds = request.POST.get("beds")
        room.room_number = room_n
        room.beds = beds
        room.save()
        messages.success(request, "Room Updated!")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {"room":room}
    return render(request, "admin/update_room.html", context)
    

def delete_room(request, room_id):
    room = Room.objects.get(id = room_id)
    room.delete()
    return redirect("app:manage-rooms")