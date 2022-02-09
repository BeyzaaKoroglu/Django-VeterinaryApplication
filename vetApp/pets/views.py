from rest_framework import viewsets

from pets.models import Pet, PetOwner
from pets.serializers import PetOwnerSerializer, PetSerializer

from pets.filters import PetOwnerFilter, PetFilter


class PetOwnerViewSet(viewsets.ModelViewSet):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerSerializer
    filterset_class = PetOwnerFilter


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filterset_class = PetFilter
