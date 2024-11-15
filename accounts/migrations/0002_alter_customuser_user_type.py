# Generated by Django 5.1.1 on 2024-11-15 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[("Owner", "Owner"), ("Tenant", "Tenant")], max_length=20
            ),
        ),
    ]