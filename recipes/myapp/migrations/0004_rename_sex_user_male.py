# Generated by Django 5.1.1 on 2024-10-13 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_choice_selected_category_recipes_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='sex',
            new_name='male',
        ),
    ]