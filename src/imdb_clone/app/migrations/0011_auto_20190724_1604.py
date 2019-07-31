# Generated by Django 2.2.3 on 2019-07-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190724_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=264, unique=True)),
                ('movie_actor', models.ManyToManyField(to='app.Actors')),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]