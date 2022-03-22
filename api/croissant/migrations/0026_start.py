# Generated by Django 4.0.3 on 2022-03-21 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0025_alter_layer_options_remove_layer_start_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('using_time', models.BooleanField()),
                ('layer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start', to='croissant.layer')),
            ],
        ),
    ]
