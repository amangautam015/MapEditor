# Generated by Django 2.2.5 on 2019-09-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20190907_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rectangle',
            name='orientation',
            field=models.IntegerField(choices=[(0, 'XY'), (1, 'ZX'), (2, 'ZY')], default=0),
        ),
    ]
