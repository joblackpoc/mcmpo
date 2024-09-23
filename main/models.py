from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Header(models.Model):
    header_title = models.CharField(max_length=40)
    header_description = CKEditor5Field(config_name='extends')
    header_image = models.ImageField(upload_to='header')

    def __str__(self):
        return self.header_title