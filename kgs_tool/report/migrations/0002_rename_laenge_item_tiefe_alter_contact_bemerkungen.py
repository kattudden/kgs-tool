# Generated by Django 4.0.4 on 2022-05-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='laenge',
            new_name='tiefe',
        ),
        migrations.AlterField(
            model_name='contact',
            name='bemerkungen',
            field=models.TextField(null=True),
        ),
    ]
