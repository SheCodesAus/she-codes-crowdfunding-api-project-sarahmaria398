from io import open_code
from django.db import models
from django.contrib.auth import get_user_model


class Pledge(models.Model):
    amount = models.TimeField()
    comment = models.CharField(max_length=200)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE, 
        related_name='pledges'
    )
    supporter = models.ForeignKey(get_user_model(), 
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.TimeField()
    image = models.URLField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(get_user_model(), 
    on_delete=models.CASCADE, 
    related_name='owner_projects'
    )



