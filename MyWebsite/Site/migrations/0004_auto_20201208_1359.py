# Generated by Django 3.1.4 on 2020-12-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0003_auto_20201208_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfoliopost',
            old_name='GitHub Link',
            new_name='GitHub link',
        ),
        migrations.RenameField(
            model_name='portfoliopost',
            old_name='PlayStore Link',
            new_name='Playstore Link',
        ),
        migrations.RenameField(
            model_name='portfoliopost',
            old_name='description',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='portfoliopost',
            name='image',
            field=models.ImageField(upload_to='Site/images'),
        ),
    ]