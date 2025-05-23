from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

phone_validator = RegexValidator (
        regex=r'^(\+995|0)?5\d{8}$',
        message= "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=9, validators=[phone_validator], unique=True)


    def __str__(self):
        return self.username