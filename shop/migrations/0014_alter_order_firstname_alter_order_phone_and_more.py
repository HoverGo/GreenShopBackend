# Generated by Django 4.2.6 on 2023-11-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_rename_title_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='firstName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='secondName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
