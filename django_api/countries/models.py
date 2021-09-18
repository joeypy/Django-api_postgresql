from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, blank=False)
    capital = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)
        verbose_name = "country"
        verbose_name_plural = "countries"
