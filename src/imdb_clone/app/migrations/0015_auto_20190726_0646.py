# Generated by Django 2.2.3 on 2019-07-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190724_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=264, unique=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('DOB', models.DateField()),
                ('Bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=264, unique=True)),
                ('lang', models.CharField(choices=[('ENG', 'English'), ('TEL', 'Teleugu'), ('HIN', 'Hindhi')], max_length=3)),
                ('gener', models.CharField(choices=[('Act', 'Action'), ('Adv', 'Adventure'), ('Ani', 'Animation'), ('Com', 'Comedy'), ('Cri', 'Crime'), ('Dra', 'Drama'), ('Fam', 'Family'), ('Fan', 'Fantasy'), ('Hor', 'Horror'), ('Mys', 'Mystrey'), ('Thr', 'Thriller'), ('Sci', 'Sci-fi')], max_length=3)),
                ('status', models.CharField(choices=[('RA', 'Recently Added'), ('TR', 'Top Rated'), ('MW', 'Most Watched')], max_length=2)),
                ('release_date', models.DateField()),
                ('plot', models.TextField(max_length=1024)),
                ('movie_image', models.ImageField(upload_to='media')),
                ('movie_actor', models.ManyToManyField(to='app.Actor')),
            ],
        ),
        migrations.RemoveField(
            model_name='movi',
            name='movie_actor',
        ),
        migrations.RemoveField(
            model_name='moviedetails',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Actor_det',
        ),
        migrations.DeleteModel(
            name='Actors',
        ),
        migrations.DeleteModel(
            name='Movi',
        ),
        migrations.DeleteModel(
            name='MovieDetails',
        ),
    ]
