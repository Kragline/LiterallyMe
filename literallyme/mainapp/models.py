from django.db import models
from django.urls import reverse


# all slugs are setted automatucly
# view in admin.py
class Actor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%d/%m/%Y')
    create_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('about_actor', kwargs={'actor_slug': self.slug})

    class Meta:
        verbose_name = 'Actors (they are literally me)'
        verbose_name_plural = 'Actors (they are literally me)'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Categories (literally me)'
        verbose_name_plural = 'Categories (literally me)'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    plot = models.TextField(blank=True)
    release_date = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/%d/%m/%Y')
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    actors = models.ManyToManyField(Actor, related_name='movies') # related_name is for finding each actors movies (actor.movies)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about_movie', kwargs={'movie_slug': self.slug})

    class Meta:
        verbose_name = 'Movies (literally me)'
        verbose_name_plural = 'Movies (literally me)'

        ordering = ['-create_time']
