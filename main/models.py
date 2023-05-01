from django.db import models

class Post(models.Model):
    title = models.CharField(max_length= 200)
    writer = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    feel = models.CharField(max_length= 30,null=True)
    weather = models.CharField(max_length= 30,null=True)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary (self):
        return self.body[:20]    
# Create your models here.
