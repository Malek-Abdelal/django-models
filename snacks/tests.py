from django.test import TestCase
from django.urls import path, reverse
# Create your tests here.

class TestSnack(TestCase):
    
    def test_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')