from django.db import models

class GamesNews(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    anio = models.IntegerField()
    games = models.TextChoices
   
    def __str__(self):
        return f'{self.title} {self.anio}'