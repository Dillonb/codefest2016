from django.db import models

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey("UVMUser")
    event = models.ForeignKey("Event")
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
