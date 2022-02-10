from rest_framework import viewsets, permissions, mixins

from pets.filters import PetFilter, PetOwnerFilter
from pets.models import Pet, PetOwner
from pets.serializers import PetOwnerSerializer, PetSerializer
from rest_framework.viewsets import GenericViewSet


class AdminPetOwnerViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAdminUser,
    )
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerSerializer
    filterset_class = PetOwnerFilter


class PetOwnerViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                    mixins.UpdateModelMixin,GenericViewSet):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerSerializer
    filterset_class = PetOwnerFilter


class AdminPetViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAdminUser,
    )
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filterset_class = PetFilter


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filterset_class = PetFilter
