# Generated by Django 5.1.1 on 2024-10-07 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cooking_steps', models.TextField()),
                ('cooking_time', models.TimeField()),
                ('image', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=100)),
                ('products', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipes_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.TextField()),
                ('category_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recipes')),
                ('selected_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recipes_category')),
            ],
        ),
    ]