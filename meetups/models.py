from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return f'{self.name} ({self.address})'
    

class Participant(models.Model):
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f'{self.email}'


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')
    participants = models.ManyToManyField(Participant, blank=True, null=True)
    organizer = models.EmailField()
    date = models.DateField()
    
    def __str__(self) -> str:
        return f'{self.title} - {self.location}'