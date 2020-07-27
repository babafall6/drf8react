from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    USER_PROFILE = (
        ("ADMIN", "Administrateur"),
        ("BANK", "Banque"),
        ("RPC", "Responsable Point Collecte"),
        ("PROD", "Producteur"),
        ("COM", "Commercant"),
        ("MAN_MARKET", "Manager Marché"),
        ("TIER", "Tier"),
    )

    privilege = models.CharField(max_length=20, default="PROD", choices=USER_PROFILE)

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)

    def __str__(self):
        return self.privilege
