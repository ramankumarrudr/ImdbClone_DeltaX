# Generated by Django 2.2.3 on 2019-07-24 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190724_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Actor_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=264)),
                ('DOB', models.DateField()),
                ('Bio', models.TextField()),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Actor')),
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
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Actor')),
            ],
        ),
        migrations.DeleteModel(
            name='Actor_new',
        ),
    ]
