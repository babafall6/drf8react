from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    USER_PROFILE = (
        (1, "Administrateur"),
        (2, "Banque"),
        (3, "Responsable Point Collecte"),
        (4, "Producteur"),
        (5, "Commercant"),
        (6, "Manager Marché"),
        (7, "Tiers"),
    )

    profile = models.PositiveSmallIntegerField(choices=USER_PROFILE, default=3)
    full_name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.full_name
