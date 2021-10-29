from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Profile


class AccountsTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='user',
                                                         email='user@google.com',
                                                         password='user123456789'
                                                         )
        self.profile = Profile.objects.create(user_id=1, phone_number=123456789, address='address',
                                              postal_code=12345, city='city', country='country')
        self.client.login(username='user', password='user123456789')
        self.response_login = self.client.get('/accounts/login/')
        self.response_profile = self.client.get('/accounts/profile/')

    def test_login_view(self):
        self.assertEqual(str(self.response_login.context['user']), 'user')

    def test_login_template(self):
        self.assertTemplateUsed(self.response_login, 'registration/login.html')

    def test_login_status_code(self):
        self.assertEqual(self.response_login.status_code, 200)

    def test_profile_contains_correct_html(self):
        self.assertContains(self.response_profile, 'Profile')

    def test_profile_status_code(self):
        self.assertEqual(self.response_profile.status_code, 200)

    def test_profile_template(self):
        self.assertTemplateUsed(self.response_profile, 'accounts/profile.html')

    def test_profile_content(self):
        self.assertEqual(self.profile.city, 'city')

    def test_profile_doesnt_contains_correct_html(self):
        self.assertNotContains(self.response_profile, 'carts')
