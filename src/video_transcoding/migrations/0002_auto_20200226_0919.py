# Generated by Django 3.0.3 on 2020-02-26 09:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_transcoding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='source',
            field=models.URLField(validators=[django.core.validators.URLValidator(schemes=('http', 'https'))]),
        ),
    ]
