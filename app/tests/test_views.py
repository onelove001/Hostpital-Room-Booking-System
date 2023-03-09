from django.test import TestCase, Client
from django.urls import reverse
from app.models import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_home_route_GET(self):
        response = self.client.get(reverse("app:home-route"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/home_route.html")


    def test_contact_route_GET(self):
        response = self.client.get(reverse("app:contact-route"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/contact_route.html")

    
    def test_blog_route_GET(self):
        response = self.client.get(reverse("app:blog-route"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/blog_route.html")


    def test_faq_route_GET(self):
        response = self.client.get(reverse("app:faq-route"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/faq_route.html")
