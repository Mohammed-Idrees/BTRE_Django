# Generated by Django 3.1.3 on 2020-11-24 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='relator',
            new_name='realtor',
        ),
    ]
