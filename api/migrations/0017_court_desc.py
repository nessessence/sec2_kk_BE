# Generated by Django 3.0.2 on 2020-02-01 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200201_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
