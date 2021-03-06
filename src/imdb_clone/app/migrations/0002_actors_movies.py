# Generated by Django 2.2.3 on 2019-07-24 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=264, unique=True)),
                ('year_of_release', models.PositiveIntegerField()),
                ('plot', models.TextField()),
                ('Actor', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=264)),
                ('DOB', models.DateField()),
                ('Bio', models.TextField()),
                ('Actor', models.ManyToManyField(to='app.Movies')),
            ],
        ),
    ]
