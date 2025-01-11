from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=30, null=False) 
    GENRE_CHOICES = [
        ('T', 'Terror'),
        ('C', 'Comedia'),
        ('A', 'Accion'),
    ]
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, null=False) 
    director_name = models.CharField(max_length=30, null=False) 
    publication_year = models.DateField()
    synopsis = models.TextField() 
    
    def __str__(self):
        return self.title
