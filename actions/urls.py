from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .ftp import connect_with_ftp
from .trigger_processes import trigger_steps
from .archive_article import Archived_article_attribute_view
from .providers import Provider_viewset, Provider_meta_data_FTP_viewset, Provider_meta_data_API_viewset
from .step1 import start_step1

router = DefaultRouter()
router.register('archive-article', Archived_article_attribute_view)
router.register('providers-ftp', Provider_meta_data_FTP_viewset)
router.register('providers-api', Provider_meta_data_API_viewset)

urlpatterns = [
    path('', include(router.urls)),
    path('connect-with-ftp', connect_with_ftp),
    path('dry-run', trigger_steps),
    path('step1', start_step1)
]
