from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import connectWithFTP

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('welcome', connectWithFTP),
]
