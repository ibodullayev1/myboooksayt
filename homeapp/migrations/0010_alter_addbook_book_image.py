# Generated by Django 5.1.3 on 2024-12-24 14:22

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0009_addbook_delete_bookcomment_remove_sotish_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='book_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to='image/', verbose_name='Kitob rasmi'),
        ),
    ]
