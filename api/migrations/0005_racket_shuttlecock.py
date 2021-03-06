# Generated by Django 3.0.2 on 2020-01-31 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200130_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shuttlecock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shuttlecocks', to='api.Court')),
            ],
        ),
        migrations.CreateModel(
            name='Racket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rackets', to='api.Court')),
            ],
        ),
    ]
