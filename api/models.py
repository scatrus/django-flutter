from django.db import models

class User(models.Model):
    codigo = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
