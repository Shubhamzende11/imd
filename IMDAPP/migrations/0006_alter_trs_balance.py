# Generated by Django 4.1.2 on 2022-12-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMDAPP', '0005_alter_trs_qty_trs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trs',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
    ]