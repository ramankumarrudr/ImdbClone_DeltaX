# Generated by Django 2.2.3 on 2019-07-24 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_actors_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=264)),
                ('DOB', models.DateField()),
                ('Bio', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Actors',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
    ]
