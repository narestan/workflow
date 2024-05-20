# reqmat/models.py

from django.db import models
from django.conf import settings
from materials.models import Item

class MaterialRequest(models.Model):
    STATUS_CHOICES = (
        ('Created', 'Created'),
        ('Professional Review', 'Professional Review'),
        ('Commercial Review', 'Commercial Review'),
        ('Managerial Review', 'Managerial Review'),
        ('Accounting Review', 'Accounting Review'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    DEPARTMENT_CHOICES = (
        ('Profit', 'Profit'),
        ('Glass', 'Glass'),
        ('Other', 'Other'),
    )

    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    description = models.TextField()
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Created')

    class Meta:
        abstract = True

class ProfitRequest(MaterialRequest):
    materials = models.ManyToManyField(Item, related_name='profit_requests')
    profit_estimate = models.DecimalField(max_digits=10, decimal_places=2)

class GlassRequest(MaterialRequest):
    materials = models.ManyToManyField(Item, related_name='glass_requests')
    dimensions = models.CharField(max_length=100)

class OtherRequest(MaterialRequest):
    materials = models.ManyToManyField(Item, related_name='other_requests')
    details = models.TextField()
