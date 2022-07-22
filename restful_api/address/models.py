from django.db import models

# Create your models here.


class Addresses(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=15)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
