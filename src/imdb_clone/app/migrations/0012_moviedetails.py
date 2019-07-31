# Generated by Django 2.2.3 on 2019-07-24 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190724_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.PositiveIntegerField()),
                ('plot', models.TextField(max_length='1024')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Movi')),
            ],
        ),
    ]