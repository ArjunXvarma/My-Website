# Generated by Django 3.1.4 on 2020-12-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_portfoliopost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopost',
            name='image',
            field=models.ImageField(default='', height_field=571, upload_to='Site/images', width_field=692),
        ),
    ]