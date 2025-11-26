from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField(max_length=4)

    def __str__(self):
        return self.email