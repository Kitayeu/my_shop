from django.test import TestCase
from django.urls import reverse

from .models import Order


class OrdersTests(TestCase):

    def setUp(self) -> None:
        self.order = Order.objects.create(first_name='user', last_name='user', email='user@google.com',
                                          telephone=123456789, address='address', postal_code=12345, city='city',
                                          country='country', note='new note', transport_cost=10)
        self.response = self.client.get(reverse('orders:order_create'))

    def test_orders_create_contains_correct_html(self):
        self.assertContains(self.response, 'Delivery information')

    def test_orders_create_template(self):
        self.assertTemplateUsed(self.response, 'orders/order_create.html')

    def test_orders_create_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_orders_create_content(self):
        self.assertEqual(self.order.postal_code, 12345)

    def test_orders_create_doesnt_contains_correct_html(self):
        self.assertNotContains(self.response, 'Hi')
