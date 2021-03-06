# Generated by Django 2.2.5 on 2019-09-07 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='cube', max_length=100)),
                ('length', models.FloatField(default=1.0)),
                ('x_coordinate', models.FloatField(default=0.0)),
                ('y_coordinate', models.FloatField(default=0.0)),
                ('z_coordinate', models.FloatField(default=0.0)),
                ('texID', models.IntegerField(default=0)),
                ('mass', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Rectangle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='rectangle', max_length=100)),
                ('length', models.FloatField(default=1.0)),
                ('breaddth', models.FloatField(default=1.0)),
                ('x_coordinate', models.FloatField(default=0.0)),
                ('y_coordinate', models.FloatField(default=0.0)),
                ('z_coordinate', models.FloatField(default=0.0)),
                ('texID', models.IntegerField(default=0)),
                ('mass', models.FloatField(default=0.0)),
                ('orientation', models.IntegerField(choices=[('XY', 0), ('ZX', 1), ('ZY', 2)], default=0)),
            ],
        ),
    ]
