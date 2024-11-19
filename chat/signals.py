from django.db.models.signals import post_save
from django.dispatch import receiver
from building.models import Building
from .models import ChatRoom

@receiver(post_save, sender=Building)
def create_chat_room(sender, instance, created, **kwargs):
    if created:
        ChatRoom.objects.create(
            building=instance,
            name=f"Chat for {instance.name}"
        )