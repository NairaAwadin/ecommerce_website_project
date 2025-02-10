from django.db import models
#from django.contrib.auth.models import User


class product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    img = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name