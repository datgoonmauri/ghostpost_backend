from django.conf.urls import include, url
from rest_framework import routers

from api.views import PostItemViewSet

router = routers.DefaultRouter()

router.register(r"PostItem", PostItemViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]
