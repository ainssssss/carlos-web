# Generated by Django 5.0.4 on 2024-04-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Context',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='book',
            name='Picture',
            field=models.CharField(max_length=800),
        ),
    ]