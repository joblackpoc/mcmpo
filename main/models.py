from django.db import models
from django_ckeditors.fields import CKEditorsField
# Create your models here.
class Header(models.Model):
    header_title = models.CharField(max_length=40)
    header_description = CKEditorsField(blank=True, null=True)

    header_image = models.ImageField(upload_to = 'header')

    def __str__(self):
        return self.header_title