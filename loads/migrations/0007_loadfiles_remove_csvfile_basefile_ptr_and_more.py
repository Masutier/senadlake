# Generated by Django 4.2 on 2023-04-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0006_basefile_delete_loadfiles_csvfile_jsonfile_pdffile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('file_link', models.CharField(max_length=250, null=True)),
                ('description', models.CharField(max_length=2500, null=True)),
                ('autority', models.CharField(choices=[('Oficial', 'Oficial'), ('Comunidad', 'Comunidad'), ('Privado', 'Privado')], max_length=80)),
                ('category', models.CharField(choices=[('Ciencia', 'Ciencia'), ('Comercio', 'Comercio'), ('Cultura', 'Cultura'), ('Educacion', 'Educacion'), ('Medicina', 'Medicina')], max_length=80)),
                ('file_type', models.CharField(choices=[('csv', 'csv'), ('json', 'json'), ('xls', 'xls'), ('xlsx', 'xlsx'), ('pdf', 'pdf')], max_length=10)),
                ('territory', models.CharField(choices=[('Nacional', 'Nacional'), ('Departamento', 'Departamento'), ('Municipio', 'Municipio'), ('Pueblo', 'Pueblo'), ('Zona', 'Zona'), ('Barrio', 'Barrio')], max_length=20)),
                ('downloads', models.IntegerField(null=True)),
                ('views', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('clasify_at', models.DateTimeField(null=True)),
                ('published_at', models.DateTimeField(null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='csvfile',
            name='basefile_ptr',
        ),
        migrations.RemoveField(
            model_name='jsonfile',
            name='basefile_ptr',
        ),
        migrations.RemoveField(
            model_name='pdffile',
            name='basefile_ptr',
        ),
        migrations.RemoveField(
            model_name='xlsxfile',
            name='basefile_ptr',
        ),
        migrations.DeleteModel(
            name='BaseFile',
        ),
        migrations.DeleteModel(
            name='CsvFile',
        ),
        migrations.DeleteModel(
            name='JsonFile',
        ),
        migrations.DeleteModel(
            name='PdfFile',
        ),
        migrations.DeleteModel(
            name='XlsxFile',
        ),
    ]
