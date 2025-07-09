from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import GroupViewSet

router = SimpleRouter()

router.register('groups', GroupViewSet)
router.register('posts', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]