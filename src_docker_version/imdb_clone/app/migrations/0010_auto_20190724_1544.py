# Generated by Django 2.2.3 on 2019-07-24 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190724_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor_det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('DOB', models.DateField()),
                ('Bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=264, unique=True)),
                ('year_of_release', models.PositiveIntegerField()),
                ('plot', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('actor', models.ManyToManyField(to='app.Actors')),
            ],
        ),
        migrations.RemoveField(
            model_name='actor_details',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='movi',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='Actor_details',
        ),
        migrations.DeleteModel(
            name='Movi',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='webPage',
        ),
        migrations.AddField(
            model_name='actor_det',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Actors'),
        ),
    ]
