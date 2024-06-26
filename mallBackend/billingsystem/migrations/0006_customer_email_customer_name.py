# Generated by Django 5.0.4 on 2024-04-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingsystem', '0005_remove_customer_email_remove_customer_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
