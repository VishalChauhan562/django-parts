# Generated by Django 4.2.11 on 2024-05-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_month_created_on_month_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='month',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
