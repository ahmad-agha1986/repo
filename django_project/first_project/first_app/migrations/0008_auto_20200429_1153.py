# Generated by Django 3.0.3 on 2020-04-29 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_auto_20200428_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecord',
            old_name='name',
            new_name='url',
        ),
    ]
