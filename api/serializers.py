from rest_framework.serializers import HyperlinkedModelSerializer

from .models import PostItem


class PostItemSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = PostItem
        fields = ('__all__')