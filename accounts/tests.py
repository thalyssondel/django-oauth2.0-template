from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework.test import APITestCase


class HealthCheckTest(TestCase):
    @override_settings(REST_FRAMEWORK={"DEFAULT_THROTTLE_CLASSES": [], "DEFAULT_THROTTLE_RATES": {}})
    def test_health_check_returns_200(self):
        response = self.client.get(reverse("health_check"))
        self.assertEqual(response.status_code, 200)


class ExceptionsCheckTest(APITestCase):
    def test_exception_handler_format(self):
        response = self.client.get("/api/auth/login/")

        self.assertEqual(response.status_code, 405)

        self.assertIn("error", response.data)
        self.assertIn("message", response.data)
        self.assertEqual(response.data["error"], "MethodNotAllowed")
