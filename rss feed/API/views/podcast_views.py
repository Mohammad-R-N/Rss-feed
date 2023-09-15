from django.http import Http404
from rest_framework import generics
from podcasts.models import Episode,Channel
from rest_framework.pagination import PageNumberPagination
from API.serializers.podcast_serializer import EpisodeSerializer,ChannelSerializer


class ChannelListCreateView(generics.ListCreateAPIView):
    serializer_class = ChannelSerializer

    def get_queryset(self):
        queryset = Channel.objects.all()
        return queryset
