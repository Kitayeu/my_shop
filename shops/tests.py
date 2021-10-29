from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Category, Product, Review


class ShopsTests(TestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(name='category', slug='category')
        self.product = Product.objects.create(category=self.category, name='name', slug='name',
                                              image='image.jpg', description='good description',
                                              price=1, available=True)
        self.user = get_user_model().objects.create_user(username='user',
                                                         email='user@google.com',
                                                         password='user123456789'
                                                         )
        self.review = Review.objects.create(product=self.product, author=self.user, rating=5, text='good product')
        self.response_list = self.client.get(reverse('shops:product_list'))

    def test_shops_list_view(self):
        self.assertEqual(self.response_list.status_code, 200)

    def test_shops_list_template(self):
        response = self.client.get(self.category.get_absolute_url())
        self.assertTemplateUsed(response, 'shops/product/list.html')

    def test_shops_list_contains_correct_html(self):
        self.assertContains(self.response_list, 'Aqua')

    def test_shops_list_doesnt_contains_correct_html(self):
        self.assertNotContains(self.response_list, 'Hi')

    def test_shops_list_content(self):
        self.assertEqual(str(self.category), 'category')

    def test_shops_detail_response(self):
        response = self.client.get(reverse('shops:product_list_by_category', args=(self.category.slug,)))
        self.assertEqual(response.status_code, 200)

    def test_shops_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        self.assertTemplateUsed(response, 'shops/product/detail.html')

    def test_shops_detail_content(self):
        self.assertEqual(self.product.description, 'good description')

    def test_shops_review_content(self):
        self.assertEqual(self.review.text, 'good product')
