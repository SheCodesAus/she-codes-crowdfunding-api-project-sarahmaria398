from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.TimeField()
    image = models.URLField()
    date_created = models.DateTimeField()
    owner = models.CharField(max_length=200)
