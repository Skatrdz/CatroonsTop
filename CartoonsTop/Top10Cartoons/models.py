from django.db import models
from django.urls import reverse


class Top10Cartoons(models.Model):
    tittle = models.CharField(max_length=255, verbose_name="Боже мой")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_crete = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Top 10 Cartoons'
        verbose_name_plural ='Top 10 Cartoons'
        ordering = ['-time_crete', 'tittle']