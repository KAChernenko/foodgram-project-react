# Generated by Django 4.2.1 on 2023-06-08 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingridients',
            new_name='ingredients',
        ),
    ]