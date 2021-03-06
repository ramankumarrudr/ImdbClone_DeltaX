# Generated by Django 2.2.3 on 2019-07-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190724_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=264, unique=True)),
                ('year_of_release', models.PositiveIntegerField()),
                ('plot', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('actor', models.ManyToManyField(to='app.Actor')),
            ],
        ),
        migrations.AlterField(
            model_name='actor_details',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
