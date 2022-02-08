from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class PhoneNumberValidator(RegexValidator):

    regex = r"^\+[0-9]{1,3}\d{10}$"
    message = _("Format: +901234567890. ")
    flags = 0


phone_number = PhoneNumberValidator()
