# Generated by Django 4.1 on 2022-08-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_p_add_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='p_add_date',
            field=models.DateTimeField(),
        ),
    ]