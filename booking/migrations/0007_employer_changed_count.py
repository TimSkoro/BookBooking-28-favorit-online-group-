# Generated by Django 4.1.5 on 2023-01-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_rename_employers_employer_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='changed_count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
