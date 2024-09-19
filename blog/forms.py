from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from . models import Categories

class CategoriesForm(forms.Form):

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["description"].required = False

    class Meta:
         model = Categories
         fields = ('name', 'description')
         labels = {
             'name': 'Category Name',
             'description': 'Description',
         }
         widgets = {
              "description": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="Description"
              )
          }