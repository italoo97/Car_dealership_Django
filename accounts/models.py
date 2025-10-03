from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=False, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    birth = models.DateField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}" if self.first_name else self.user.username
