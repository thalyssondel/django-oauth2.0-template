from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError


def health_check(request):
    check_type = request.GET.get("check", "shallow")

    health_status = {
        "status": "healthy",
        "service": "django-oauth2.0-template",
        "timestamp": True,
    }

    if check_type == "deep":
        try:
            db_conn = connections["default"]
            db_conn.cursor()
            health_status["database"] = "connected"
        except OperationalError:
            health_status["status"] = "unhealthy"
            health_status["database"] = "disconnected"
            return JsonResponse(health_status, status=503)

    return JsonResponse(health_status, status=200)
