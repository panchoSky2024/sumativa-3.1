from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',  # Cambiado para evitar conflicto
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',  # Cambiado para evitar conflicto
        related_query_name='user',
    )

    def __str__(self):
        return self.username