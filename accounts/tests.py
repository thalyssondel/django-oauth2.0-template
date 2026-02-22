from django.test import TestCase
from django.urls import reverse

class HealthCheckTest(TestCase):
    def test_health_check_returns_200(self):
        response = self.client.get(reverse('health_check'))
        self.assertEqual(response.status_code, 200)