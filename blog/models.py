from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = CKEditor5Field('Text', config_name='extends')