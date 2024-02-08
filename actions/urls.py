from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .ftp import connect_with_ftp
from .trigger_processes import trigger_steps
from .archive_article import Archived_artical_attribute_view

router = DefaultRouter()
router.register('archive-article', Archived_artical_attribute_view)

urlpatterns = [
    path('', include(router.urls)),
    path('connect-with-ftp', connect_with_ftp),
    path('dry-run', trigger_steps),
]
