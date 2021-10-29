from django.test import TestCase
from django.urls import reverse


class CartsTests(TestCase):

    def setUp(self) -> None:
        self.response = self.client.get(reverse('carts:cart_detail'))

    def test_carts_contains_correct_html(self):
        self.assertContains(self.response, 'Your order')

    def test_carts_template(self):
        self.assertTemplateUsed(self.response, 'carts/detail.html')

    def test_carts_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_carts_doesnt_contains_correct_html(self):
        self.assertNotContains(self.response, 'Profile')
