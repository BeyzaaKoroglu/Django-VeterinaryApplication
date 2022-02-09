from rest_framework import serializers

from pets.models import Pet, PetOwner


class PetOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = (
            "id",
            "full_name",
            "address",
            "phone",
            "email",
            "created_at",
            "modified_at",
        )


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = (
            "id",
            "owner",
            "type",
            "genus",
            "age",
            "description",
            "created_at",
            "modified_at",
        )
