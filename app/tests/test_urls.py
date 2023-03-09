from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import *

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

    
    def test_gym_route_is_resolved(self):
        
        url = reverse("app:gym-route")
        path = (resolve(url))
        self.assertEquals(path.func, my_gym_route)
