# Generated by Django 4.1.6 on 2023-02-15 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbookPage', '0008_alter_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='id',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
