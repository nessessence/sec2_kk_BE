# Generated by Django 3.0.3 on 2020-02-19 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20200219_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='court',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='api.Court'),
            preserve_default=False,
        ),
    ]
