# Generated by Django 3.1.4 on 2020-12-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0009_auto_20201211_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopost',
            name='GitHub link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='portfoliopost',
            name='Playstore Link',
            field=models.URLField(),
        ),
    ]