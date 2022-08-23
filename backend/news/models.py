from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.TextField(max_length=255)
    def __str__(self):
        return self.name


class News(models.Model):
    Title = models.TextField(max_length=255)
    img = models.URLField()
    link = models.URLField()
    network = models.ForeignKey(Channel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title