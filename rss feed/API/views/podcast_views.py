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
    


class ChannelDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChannelSerializer

    def get_object(self):
        pk = self.kwargs["pk"]

        queryset = Channel.objects.filter(pk=pk)

        if not queryset.exists():
            raise Http404("Podcast not found")

        return queryset.first()


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000



class EpisodeListCreateView(generics.ListCreateAPIView):
    serializer_class = EpisodeSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        podcast_pk = self.kwargs["pk"]

        queryset = Episode.objects.filter(podcast__pk=podcast_pk)

        if not queryset.exists():
            raise Http404("Podcast episode not found")

        return queryset
    


class EpisodeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EpisodeSerializer

    def get_object(self):
        pk = self.kwargs["pk"]

        queryset = Episode.objects.filter(pk=pk)

        if not queryset.exists():
            raise Http404("Podcast episode not found")

        return queryset.first()