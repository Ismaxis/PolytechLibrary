# Generated by Django 4.0.6 on 2022-07-06 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_direction_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='institution',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.institution'),
            preserve_default=False,
        ),
    ]
