# materials/models.py

from django.db import models

class CategoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    def __str__(self):
        return self.name

class Item(models.Model):
    item = models.CharField(max_length=100)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    unit = models.CharField(max_length=10)
    category = models.ForeignKey(CategoryItem, on_delete=models.CASCADE)
    code = models.IntegerField(blank=True)
    def __str__(self):
        return self.item
