from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import About


class AboutForm(forms.ModelForm):
      """Form for comments to the article."""

      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['about_content'].required = False

      class Meta:
          model = About
          fields = ('about_title', 'about_intro', 'about_image_content', 
                    'about_header', 'about_content', 'about_story', 'about_story_detail', 'about_image_story',
                    'about_goal', 'about_goal_detail', 'about_image_goal')
          widgets = {
              'about_content': CKEditor5Widget(
                  attrs={'class': 'django_ckeditor_5'}, config_name='extends'
              )
          }