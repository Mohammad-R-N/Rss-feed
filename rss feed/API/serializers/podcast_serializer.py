from rest_framework.serializers import ModelSerializer
from podcasts.models import *



class CategorySerializer(ModelSerializer):

    class Meta:
        model=Category
        fields=[
            "name",
        ]


class XMLSerializer(ModelSerializer):

    class Meta:
        model = XML
        fields = [
            "link",
            "name",
        ]


class ChannelSerializer(ModelSerializer):

    class Meta:
        model = Channel
        fields = [
            "title",
            "description",
            "language",
            "copyright",
            "subtitle",
            "author",
            "summary",
            "image",
            "keywords",
            "ownerName",
            "ownerEmail",
            "isExplicit",
            "xml",
            "follow",
            "category"
        ]
