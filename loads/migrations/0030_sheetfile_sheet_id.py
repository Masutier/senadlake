# Generated by Django 4.2 on 2023-05-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0029_remove_sheetfile_sheet_alter_sheetfile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheetfile',
            name='sheet_id',
            field=models.IntegerField(null=True),
        ),
    ]
