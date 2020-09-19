from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.FileField(blank=True)
    url = models.URLField(blank=True)
    time = models.DateField()

    def __str__(self):
        return self.title
