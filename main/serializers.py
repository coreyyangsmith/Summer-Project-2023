from rest_framework import serializers
from .models import *

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('id', 'code', 'name',
                  'image', 'sector',
                  'created_at', 'updated_at')
