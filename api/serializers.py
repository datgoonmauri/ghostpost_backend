from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Post


class PostSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('__all__')