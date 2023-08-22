from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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

    def get_absolute_url_for_update(self):
        return reverse('update_actor', kwargs={'actor_slug': self.slug})

    def get_absolute_url_for_delete(self):
        return reverse('delete_actor', kwargs={'actor_slug': self.slug})

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
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='movies')
    rating = models.IntegerField(default=1, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about_movie', kwargs={'movie_slug': self.slug})

    def get_absolute_url_for_update(self):
        return reverse('update_movie', kwargs={'movie_slug': self.slug})

    def get_absolute_url_for_delete(self):
        return reverse('delete_movie', kwargs={'movie_slug': self.slug})

    class Meta:
        verbose_name = 'Movies (literally me)'
        verbose_name_plural = 'Movies (literally me)'


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url_for_update(self):
        return reverse('update_comment', kwargs={'comment_id': self.pk, 'movie_slug': self.movie.slug})

    def get_absolute_url_for_delete(self):
        return reverse('delete_comment', kwargs={'comment_id': self.pk, 'movie_slug': self.movie.slug})
