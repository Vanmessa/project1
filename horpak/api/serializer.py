from rest_framework import serializers
from horpak.models import Horpakdetail

class HorpakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horpakdetail
        fields = "__all__"