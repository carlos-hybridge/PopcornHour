from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

class RoleUser(AbstractUser):
    roles = models.ManyToManyField(Role, related_name='users', blank=True)

    def __str__(self):
        return f'{self.username} - {self.roles.first()}'

    def is_admin(self):
        return self.roles.filter(name='admin').exists()

    def is_moderator(self):
        return self.roles.filter(name='moderator').exists()

    class Meta:
        verbose_name = 'Role User'
        verbose_name_plural = 'Role Users'