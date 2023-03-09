from django.urls import path
from .views import *
from .admin_views import *

app_name = "app"

urlpatterns = [

    # User working routes
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
    path("create-class-route", create_class_route, name="create-class-route"),
    path("create-coach-route", create_coach_route, name="create-coach-route"),
    path("create-membership-route", create_membership_route, name="create-membership-route"),
    path("admin-dashboard-route", admin_dashboard_route, name="admin-dashboard-route"),
    path("approve-or-dissaprove-route/<str:gym_id>", approve_or_dissaprove_route, name="approve-or-dissaprove-route"),
]


