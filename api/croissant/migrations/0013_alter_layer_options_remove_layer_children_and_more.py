# Generated by Django 4.0.3 on 2022-03-20 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0012_alter_layer_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layer',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='layer',
            name='children',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='start_time',
        ),
    ]