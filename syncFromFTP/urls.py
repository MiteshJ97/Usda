from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import connect_with_ftp, dry_run_steps

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('connect-with-ftp', connect_with_ftp),
    path('dry-run', dry_run_steps),
]
