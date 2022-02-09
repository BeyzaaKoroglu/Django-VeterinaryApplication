from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from core.utils import PhoneNumberValidator


class PetOwner(BaseAbstractModel):

    phone_number_validator = PhoneNumberValidator()
    email_validator = EmailValidator()

    full_name = models.CharField(max_length=100, verbose_name=_("Full Name"))
    address = models.CharField(
        max_length=1000, verbose_name=_("Address"), null=True, blank=True
    )
    phone = models.CharField(
        max_length=20,
        verbose_name=_("Phone Number"),
        validators=[phone_number_validator],
        help_text=_("Phone number format: +901234567890."),
    )
    email = models.EmailField(
        verbose_name=_("E-mail"), validators=[email_validator], null=True, blank=True
    )

    class Meta:
        verbose_name = _("Pet Owner")
        verbose_name_plural = _("Pet Owners")

    def __str__(self):
        return f"{self.full_name}"


class Pet(BaseAbstractModel):

    owner = models.ForeignKey(
        "PetOwner", verbose_name=_("Pet Owner"), on_delete=models.PROTECT
    )
    type = models.CharField(max_length=50, verbose_name=_("Type"))
    genus = models.CharField(max_length=50, verbose_name=_("Genus"))
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    age = models.PositiveSmallIntegerField(verbose_name=_("Age"))
    description = models.TextField(
        max_length=2000, verbose_name=_("Description"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("pet")
        verbose_name_plural = _("pets")

    def __str__(self):
        return f"{self.owner} - {self.name}"
