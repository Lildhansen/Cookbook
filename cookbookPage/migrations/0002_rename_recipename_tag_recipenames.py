# Generated by Django 4.1.6 on 2023-06-02 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbookPage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='recipeName',
            new_name='recipeNames',
        ),
    ]
