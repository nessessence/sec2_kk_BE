# Generated by Django 3.0.2 on 2020-02-01 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200131_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='court',
            old_name='isVerified',
            new_name='is_verified',
        ),
        migrations.RenameField(
            model_name='extendeduser',
            old_name='isVerified',
            new_name='is_verified',
        ),
        migrations.RenameField(
            model_name='shuttlecock',
            old_name='countPerUnit',
            new_name='count_per_unit',
        ),
    ]