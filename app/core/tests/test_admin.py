from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse



class AdminSiteTest(TestCase):

    def setUp(self):
        self.Client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mptdev.com', 
            password='password123')

        self.Client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@mptdev.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.Client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        #/admin/core/user/args:
        res = self.Client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_crea_user_page(self):
        """Test that the creeate user page works"""
        url = reverse('admin:core_user_add')
        res = self.Client.get(url)

        self.assertEqual(res.status_code, 200)