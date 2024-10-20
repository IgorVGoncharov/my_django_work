# Generated by Django 5.1.1 on 2024-10-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_recipes_image_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Selection',
        ),
        migrations.RemoveField(
            model_name='recipes_category',
            name='category_image',
        ),
        migrations.AddField(
            model_name='recipes_category',
            name='image',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]