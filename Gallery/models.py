from django.db import models

# Create your models here.
class PhotoModel(models.Model):
    category = models.CharField(max_length = 100)
    caption = models.CharField(max_length = 1000)
    image = models.ImageField(upload_to='gall', blank=True)
    video = models.FileField(upload_to='gall', blank=True)

    def __str__(self):
        return self.caption
