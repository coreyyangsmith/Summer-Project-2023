from rest_framework import serializers
from .models import *

class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = ('id', 'code', 'name',
                  'image', 'sector',
                  'created_at', 'updated_at')
