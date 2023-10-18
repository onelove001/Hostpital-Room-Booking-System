from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import *
from app.staff_views import *

class TestUrls(SimpleTestCase):

    def test_home_route_is_resolved(self):

        url = reverse("app:home-route")
        path = (resolve(url))
        self.assertEquals(path.func, home_route)

    def test_contact_route_is_resolved(self):
        
        url = reverse("app:contact-route")
        path = (resolve(url))
        self.assertEquals(path.func, contact_route)

    
    def test_faq_route_is_resolved(self):
        
        url = reverse("app:faq-route")
        path = (resolve(url))
        self.assertEquals(path.func, faq_route)

    
    def test_dashboard_route_is_resolved(self):
        
        url = reverse("app:staff-dashboard-route")
        path = (resolve(url))
        self.assertEquals(path.func, staff_dashboard_route)


    def test_add_patient_is_resolved(self):
        
        url = reverse("app:add-patient")
        path = (resolve(url))
        self.assertEquals(path.func, add_patient)


    def test_manage_patients_is_resolved(self):
        
        url = reverse("app:manage-patients")
        path = (resolve(url))
        self.assertEquals(path.func, manage_patients)
