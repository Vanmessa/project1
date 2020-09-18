from django.urls import path
from horpak.api.views import HorpakListApi

urlpatterns = [
    path("horpaks/",HorpakListApi.as_view(),name ="horpakname"),
]
