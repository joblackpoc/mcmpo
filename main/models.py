from django.db import models

# Create your models here.
class Header(models.Model):
    header_title = models.CharField(max_length=40)
    header_description = models.CharField(max_length=100)
    header_image = models.ImageField(upload_to='header')

    def __str__(self):
        return self.header_title