from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import connectWithFTP, dryRunSteps

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('welcome', connectWithFTP),
    path('dry-run', dryRunSteps),
]
