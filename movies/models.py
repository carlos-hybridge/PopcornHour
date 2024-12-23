from django.db import models

from users.models import RoleUser


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='movies/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(RoleUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:50]}..."

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(RoleUser, on_delete=models.CASCADE)
    rating = models.FloatField()

    class Meta:
        unique_together = ('movie', 'user')

    def __str__(self):
        return f"{self.user.username}: {self.rating}"