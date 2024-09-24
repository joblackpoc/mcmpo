from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Header(models.Model):
    header_title = models.CharField(max_length=40)
    header_description = models.CharField(max_length=100)

    header_image = models.ImageField(upload_to = 'header')

    def __str__(self):
        return self.header_title
    
class About(models.Model):
    about_title = models.CharField(max_length=100)
    about_intro = models.CharField(max_length=200)
    about_image_content = models.ImageField(upload_to='about')
    about_header = models.CharField(max_length=200)
    about_content = CKEditor5Field('about_content', config_name='extends')
    about_story = models.CharField(max_length=200)
    about_story_detail = models.CharField(max_length=200)
    about_image_story = models.ImageField(upload_to='about')
    about_goal = models.CharField(max_length=200)
    about_goal_detail = models.CharField(max_length=200)
    about_image_goal = models.ImageField(upload_to='about')
