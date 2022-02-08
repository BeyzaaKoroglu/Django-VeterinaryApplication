from django.contrib import admin

from pets.models import Pet, PetOwner


class PetInline(admin.StackedInline):
    model = Pet


@admin.register(PetOwner)
class PetOwnerAdmin(admin.ModelAdmin):

    search_fields = ("full_name",)
    list_display = ("full_name", "address", "phone", "email")
    inlines = [PetInline]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):

    search_fields = ("owner__full_name", "name")
    list_display = ("owner", "name", "type", "genus", "name", "age", "description")
