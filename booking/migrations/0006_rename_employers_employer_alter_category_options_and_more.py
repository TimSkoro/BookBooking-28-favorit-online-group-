# Generated by Django 4.1.5 on 2023-01-17 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0005_alter_employers_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employers',
            new_name='Employer',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='employer',
            options={'default_related_name': 'employer_set', 'ordering': ('-user',), 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(limit_choices_to={'is_staff': True, 'is_superuser': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
