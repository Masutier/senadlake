# Generated by Django 4.2 on 2023-05-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0012_loadfiles_data_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadfiles',
            name='sheet_set',
            field=models.JSONField(null=True),
        ),
    ]
