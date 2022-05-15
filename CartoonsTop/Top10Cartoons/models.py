from django.db import models

class Top10Cartoons(models.Model):
    tittle = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_crete = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)