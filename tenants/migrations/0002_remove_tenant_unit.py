# Generated by Django 5.1.1 on 2024-11-15 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tenants", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tenant",
            name="unit",
        ),
    ]