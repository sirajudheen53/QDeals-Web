from django.db import models
from django.contrib.auth.models import User

class QUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone_number = models.CharField(max_length=13)
    provider = models.CharField(max_length=10, null=True)