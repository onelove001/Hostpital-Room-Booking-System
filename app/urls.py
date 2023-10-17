from django.urls import path
from .views import *
from .admin_views import *

app_name = "app"

urlpatterns = [

    # Patient working routes
    path("", home_route, name="home-route"),
    path("contact-route", contact_route, name="contact-route"),
    path("login-route", login_route, name="login-route"),
    path("join-route", join_route, name="join-route"),
    path("logout-route", logout_route, name="logout-route"),
    path("faq-route", faq_route, name="faq-route"),
    path("blog-route", blog_route, name="blog-route"),
    path("membership-route", membership_route, name="membership-route"),
    path("class-route", class_route, name="class-route"),
    path("coach-route", coach_route, name="coach-route"),
    path("gym-route", my_gym_route, name="gym-route"),


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
    
]


