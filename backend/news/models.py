from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.TextField(max_length=255)


class News(models.Model):
    Title = models.TextField(max_length=255)
    content = models.TextField(max_length=255)
    img = models.URLField(max_length=255)
    link = models.URLField(max_length=255)
    network = models.ForeignKey(Channel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)