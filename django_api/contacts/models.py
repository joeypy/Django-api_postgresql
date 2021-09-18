from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_picture = models.URLField(null=True)
    is_favorite  = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.name

    class Meta:
        ordering = ("id",)
        verbose_name = "contact"
        verbose_name_plural = "contacts"
