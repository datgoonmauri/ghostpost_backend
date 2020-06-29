from django.conf.urls import include, url
from rest_framework import routers

from api.views import PostViewSet

router = routers.DefaultRouter()

router.register(r"Post", PostViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]
