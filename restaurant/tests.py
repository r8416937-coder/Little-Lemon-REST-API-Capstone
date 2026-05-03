from django.urls import reverse
from django.db import IntegrityError
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Category, MenuItem, Booking


class LittleLemonAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(slug='mains', title='Mains')
        self.item = MenuItem.objects.create(title='Greek Salad', price='12.50', featured=True, category=self.category)

    def test_menu_items_are_available(self):
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Greek Salad')

    def test_booking_api_creates_booking(self):
        response = self.client.post('/api/bookings/', {
            'first_name': 'Maryam',
            'reservation_date': '2026-05-02',
            'reservation_slot': 18
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)

    def test_duplicate_booking_is_not_allowed(self):
        Booking.objects.create(first_name='A', reservation_date='2026-05-02', reservation_slot=19)
        with self.assertRaises(IntegrityError):
            Booking.objects.create(first_name='B', reservation_date='2026-05-02', reservation_slot=19)

    def test_user_registration_returns_token(self):
        response = self.client.post('/api/registration/', {
            'username': 'learner',
            'email': 'learner@example.com',
            'password': 'StrongPass123'
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('token', response.data)
