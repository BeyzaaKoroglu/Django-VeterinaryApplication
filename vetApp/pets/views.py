from rest_framework import viewsets

from pets.models import Pet, PetOwner
from pets.serializers import PetOwnerSerializer, PetSerializer


class PetOwnerViewSet(viewsets.ModelViewSet):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
