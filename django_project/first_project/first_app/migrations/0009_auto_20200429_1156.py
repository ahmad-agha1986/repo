# Generated by Django 3.0.3 on 2020-04-29 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_auto_20200429_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecord',
            old_name='url',
            new_name='webpageName',
        ),
    ]
