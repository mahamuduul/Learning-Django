from django.db import models

# Create your models here.

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
   
    github_url = models.URLField()
    live_url = models.URLField()
    author = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.title
