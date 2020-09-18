from rest_framework import generics
from horpak.models import Horpakdetail
from horpak.api.serializer import HorpakSerializer

class HorpakListApi(generics.ListCreateAPIView):
    queryset = Horpakdetail.objects.all()
    serializer_class = HorpakSerializer