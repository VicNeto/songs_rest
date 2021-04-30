from .serializer import SongModelSerializer
from .models import SongModel
from rest_framework.viewsets import ModelViewSet

class SongViewSet(ModelViewSet):
    queryset = SongModel.objects.all()
    serializer_class = SongModelSerializer
    