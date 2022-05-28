from django.db import models


class Section(models.Model):
    """The model of categories of goods"""
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """The model of the received goods"""

    name = models.CharField(max_length=100)
    received_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    measure = models.CharField(max_length=15)
    supplier_name = models.CharField(max_length=160)
    category = models.ManyToManyField(Section, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} "{self.supplier_name}"'
