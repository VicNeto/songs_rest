from .models import SongModel
from rest_framework.serializers import ModelSerializer

class SongModelSerializer(ModelSerializer):
    class Meta:
        model = SongModel
        fields = ['_id', 'name', 'artist', 'duration']

