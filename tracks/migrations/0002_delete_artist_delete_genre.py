# Generated by Django 4.2.3 on 2023-07-27 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]