from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import PostItemSerializer
from api.models import PostItem


class PostItemViewSet(ModelViewSet):
    serializer_class = PostItemSerializer
    queryset = PostItem.objects.all()

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.upvotes += 1
        post.vote_score += 1
        post.save()
        return Response({'status': 'upvote'})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        post.downvotes += 1
        post.vote_score -= 1
        post.save()
        return Response({'status': 'downvote'})

    @action(detail=False)
    def boasts(self, request, pk=None):
        qs = PostItem.objects.filter(category_choice='boast').values()
        return Response({'boasts': list(qs)})

    @action(detail=False)
    def roasts(self, request, pk=None):
        qs = PostItem.objects.filter(category_choice='roast').values()
        return Response({'roasts': list(qs)})

    @action(detail=False)
    def vote_score(self, request, pk=None):
        qs = PostItem.objects.all().order_by('-vote_score').values()
        return Response({'Vote Score': qs})