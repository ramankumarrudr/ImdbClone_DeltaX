# Generated by Django 2.2.3 on 2019-07-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190724_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_movie', models.CharField(max_length=264, unique=True)),
                ('sex', models.CharField(max_length=264)),
                ('DOB', models.DateField()),
                ('Bio', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
    ]
