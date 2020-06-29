from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import PostSerializer
from api.models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.upvote += 1
        post.vote += 1
        post.save()
        return Response({'status': 'upvote'})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        post.downvote += 1
        post.vote -= 1
        post.save()
        return Response({'status': 'downvote'})

    @action(detail=False)
    def boasts(self, request, pk=None):
        qs = Post.objects.filter(category_choice='boast').values()
        return Response({'boasts': list(qs)})

    @action(detail=False)
    def roasts(self, request, pk=None):
        qs = Post.objects.filter(category_choice='roast').values()
        return Response({'roasts': list(qs)})

    @action(detail=False)
    def vote(self, request, pk=None):
        qs = Post.objects.all().order_by('-vote').values()
        return Response({'Votes': qs})



