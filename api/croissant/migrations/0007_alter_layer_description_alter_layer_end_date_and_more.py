# Generated by Django 4.0.3 on 2022-03-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0006_alter_layer_options_rename_text_layer_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='layer',
            name='end_date',
            field=models.DateField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='layer',
            name='end_time',
            field=models.TimeField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='layer',
            name='start_date',
            field=models.DateField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='layer',
            name='start_time',
            field=models.TimeField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='layer',
            name='title',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
