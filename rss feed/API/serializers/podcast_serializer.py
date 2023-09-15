from rest_framework.serializers import ModelSerializer
from podcasts.models import *



class CategorySerializer(ModelSerializer):

    class Meta:
        model=Category
        fields=[
            "name",
        ]