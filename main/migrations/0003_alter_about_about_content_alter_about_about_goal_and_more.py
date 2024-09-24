# Generated by Django 5.1.1 on 2024-09-24 08:26

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='about_content'),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_goal',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_header',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_story',
            field=models.CharField(max_length=200),
        ),
    ]
