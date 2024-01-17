from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WelcomeMessage

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('welcome', WelcomeMessage),
]
