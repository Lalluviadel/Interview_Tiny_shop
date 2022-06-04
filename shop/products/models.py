from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db.models import Manager


class AvailableQuerySet(models.QuerySet):
    """Customizing queryset to get undeleted objects"""
    def not_deleted(self):
        return self.filter(is_deleted=False)


class AvailableManager(Manager):
    """Customizing model Manager to get undeleted objects"""
    def get_queryset(self):
        return AvailableQuerySet(self.model, using=self._db)

    def not_deleted(self):
        return self.get_queryset().not_deleted()


class Section(models.Model):
    """The model of categories of goods"""
    name = models.CharField(max_length=64)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default='1')
    is_deleted = models.BooleanField(default=False, null=False)

    # objects = AvailableManager()
    objects = Manager()
    on_site = CurrentSiteManager()

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
    site = models.ManyToManyField(Site)

    objects = Manager()
    on_site = CurrentSiteManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} "{self.supplier_name}"'
