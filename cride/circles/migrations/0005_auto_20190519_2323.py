# Generated by Django 2.0.9 on 2019-05-19 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0004_auto_20190519_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='is_public',
            new_name='is_admin',
        ),
    ]
