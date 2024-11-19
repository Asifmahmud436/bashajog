# Generated by Django 5.1.1 on 2024-11-19 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("building", "0005_alter_unit_image"),
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatroom",
            name="building",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="building.building"
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="chat_room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="chat.chatroom",
            ),
        ),
    ]
