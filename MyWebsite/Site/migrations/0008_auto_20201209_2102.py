# Generated by Django 3.1.4 on 2020-12-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0007_auto_20201209_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopost',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/'),
        ),
    ]