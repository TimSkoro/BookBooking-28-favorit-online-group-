# Generated by Django 4.1.5 on 2023-01-13 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_author_description_employers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employers',
            name='boss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.employers'),
        ),
        migrations.AlterField(
            model_name='employers',
            name='slaves',
            field=models.ManyToManyField(blank=True, null=True, to='booking.employers'),
        ),
    ]
