from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='members', null=True, blank=True)

    # Change the related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_groups",  # Unique related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions",  # Unique related_name
        related_query_name="user_permission",
    )
class Department(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='managed_department')

    def __str__(self):
        return self.name