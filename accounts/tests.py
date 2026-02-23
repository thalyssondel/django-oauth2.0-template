from django.test import TestCase, override_settings
from django.urls import reverse


class HealthCheckTest(TestCase):
    @override_settings(REST_FRAMEWORK={"DEFAULT_THROTTLE_CLASSES": [], "DEFAULT_THROTTLE_RATES": {}})
    def test_health_check_returns_200(self):
        response = self.client.get(reverse("health_check"))
        self.assertEqual(response.status_code, 200)
