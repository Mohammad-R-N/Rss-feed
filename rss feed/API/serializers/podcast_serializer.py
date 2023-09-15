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

