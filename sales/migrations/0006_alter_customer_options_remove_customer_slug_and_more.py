# Generated by Django 5.1.5 on 2025-01-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_alter_customer_options_customer_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='slug',
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(error_messages='hoppla', help_text='max 30 letters, dummy', max_length=30),
        ),
    ]
