# Generated by Django 4.2.5 on 2023-12-04 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_rename_customer_review_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='username',
            new_name='customer',
        ),
    ]