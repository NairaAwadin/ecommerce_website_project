from django.db import models

class product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    ##img = models.ImageField(upload_to ='images/', null=True)

    def __str__(self):
        return self.name
