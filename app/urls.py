from django.urls import path
from .views import *
from .admin_views import *
from .staff_views import *

app_name = "app"

urlpatterns = [

    # General routes
    path("", home_route, name="home-route"),
    path("contact-route", contact_route, name="contact-route"),
    path("login-route", login_route, name="login-route"),
    path("logout-route", logout_route, name="logout-route"),
    path("faq-route", faq_route, name="faq-route"),


    # Admin working routes
    path("admin-dashboard-route", admin_dashboard_route, name="admin-dashboard-route"),
    path("create-staff", create_staff, name="create-staff"),
    path("manage-staffs", manage_staffs, name="manage-staffs"),
    path("update-staff/<int:staff_id>", update_staff, name="update-staff"),
    path("delete-staff/<int:staff_id>", delete_staff, name="delete-staff"),
    path("create-room", create_room, name="create-room"),
    path("manage-rooms", manage_rooms, name="manage-rooms"),
    path("update-room/<int:room_id>", update_room, name="update-room"),
    path("delete-room/<int:room_id>", delete_room, name="delete-room"),
    
    # Staff working routes
    path("staff-dashboard-route", staff_dashboard_route, name="staff-dashboard-route"),
    path("add-patient", add_patient, name="add-patient"),
    path("manage-patients", manage_patients, name="manage-patients"),
    path("update-patient/<int:patient_id>", update_patient, name="update-patient"),
    path("create-medication/<int:patient_id>", create_medication, name="create-medication"),
    path("delete-patient/<int:patient_id>", delete_patient, name="delete-patient"),
    path("view-medications", view_medications, name="view-medications"),
    path("update-medication/<int:med_id>", update_medication, name="update-medication"),
    path("delete-medication/<int:med_id>", delete_medication, name="delete-medication"),
    path("available-rooms", available_rooms, name="available-rooms"),
    path("room-occupancies", room_occupancies, name="room-occupancies"),
    path("pay-bill/<int:occupant_id>", pay_bill, name="pay-bill"),
    path("view-bills", view_bills, name="view-bills"),

]


