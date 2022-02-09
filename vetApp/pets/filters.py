from django_filters import rest_framework as filters

from pets.models import Pet, PetOwner


class PetOwnerFilter(filters.FilterSet):
    class Meta:
        model = PetOwner
        fields = ("full_name",)


class PetFilter(filters.FilterSet):
    class Meta:
        model = Pet
        fields = ("owner__full_name", "name")
