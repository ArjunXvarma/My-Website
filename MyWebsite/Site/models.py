from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class PortfolioPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', max_length=255, null=True, blank=True)
    playStoreLink = models.TextField(null=True, blank=True)
    gitHubLink = models.TextField(null=True, blank=True)
    platform = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title