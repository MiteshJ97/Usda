from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .ftp import connect_with_ftp
from .trigger_processes import trigger_steps

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('connect-with-ftp', connect_with_ftp),
    path('dry-run', trigger_steps),
]
