from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.TextField(max_length=255)
    #logo = models.URLField(max_length=1000)
    #color = models.CharField(max_length=20)

    def get_news(self):
        x = Channel.objects.get(name=self.name)
        return x.news.all()

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.TextField(max_length=1000)
    img = models.URLField(max_length=1000)
    link = models.URLField(max_length=1000)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="news")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title