# Generated by Django 2.2.3 on 2019-07-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_tvshow'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='actor_image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]