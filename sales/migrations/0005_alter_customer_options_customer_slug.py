# Generated by Django 5.1.5 on 2025-01-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_bill_product_rename_second_name_customer_last_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['-first_name'], 'verbose_name': 'Kunde', 'verbose_name_plural': 'Kunden'},
        ),
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]