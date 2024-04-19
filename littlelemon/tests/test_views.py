# Inside test_views.py
from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Pizza", price=10)
        self.menu2 = Menu.objects.create(title="Burger", price=8)

    def test_getall(self):
        response = self.client.get('/api/menus/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [
            {"title": "Pizza", "price": "10.00"},
            {"title": "Burger", "price": "8.00"}
        ])
