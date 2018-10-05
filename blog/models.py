from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField( default=timezone.now )
    body = models.TextField(default='')
    image = models.ImageField(upload_to='images/')
  
    def __str__(self):
        return self.title

