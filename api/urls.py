from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, PresentationViewSet, \
    SpeakerViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='FW API',
        default_version='v1',
        description='REST API для Framework Weekend',
        contact=openapi.Contact(email='fadeddexofan@gmail.com'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_schemas = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]

router = DefaultRouter()
# Events
router.register(r'events', EventViewSet, basename='event')
# Speakers
router.register(r'speakers', SpeakerViewSet, basename='speaker')
# Presentations
router.register(r'presentations', PresentationViewSet, basename='presentation')

urlpatterns = [
    *api_schemas,
    *router.urls,
]
