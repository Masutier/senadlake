# Generated by Django 4.2 on 2023-05-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0030_sheetfile_sheet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheetfile',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
