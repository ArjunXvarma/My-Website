# Generated by Django 3.1.4 on 2020-12-08 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=571, upload_to='', width_field=692)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('PlayStore Link', models.URLField()),
                ('GitHub Link', models.URLField()),
            ],
        ),
    ]
