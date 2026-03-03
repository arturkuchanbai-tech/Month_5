
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Director(models.Model):
    fio = models.CharField(max_length=255)
    birthday = models.DateField()

    def __str__(self):
        return self.fio
    
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Film(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    release_year = models.IntegerField()
    rating = models.FloatField()
    is_hit = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    favorit_count=models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def genre_names(self):  
        return [i.name for i in self.genre.all()]

class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')  


    def __str__(self):
        return self.text
    
