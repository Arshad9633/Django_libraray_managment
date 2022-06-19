# Generated by Django 3.2.9 on 2022-02-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]
