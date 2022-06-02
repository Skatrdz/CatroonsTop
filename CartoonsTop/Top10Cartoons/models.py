from django.db import models
from django.urls import reverse


class Film(models.Model):
    title = models.CharField(max_length=255, verbose_name="title")
    slug = models.CharField(max_length=255, verbose_name="slug")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_crete = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ManyToManyField('Category', through='Film_Category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Top 10 Cartoons'
        verbose_name_plural ='Top 10 Cartoons'
        ordering = ['-time_crete', 'title']

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="title", primary_key=True)
    slug = models.CharField(max_length=255, verbose_name="slug")

    def __str__(self):
        return self.title

class Film_Category(models.Model):
    film_id = models.ForeignKey('Film', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('category_id', 'film_id')