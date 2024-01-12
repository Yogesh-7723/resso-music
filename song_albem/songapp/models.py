from django.db import models

# Create your models here.

class AddSong(models.Model):
    s_name = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    song = models.FileField(upload_to='songs/')
    
    def __str__(self):
        return self.s_name