from django.db import models
from building.models import Building
from accounts.models import CustomUser

class ChatRoom(models.Model):
    building = models.ForeignKey(Building,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat for {self.building.name}"

    class Meta:
        indexes = [
            models.Index(fields=['building'])
        ]

class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
        indexes = [
            models.Index(fields=['timestamp'])
        ]

    def __str__(self):
        return f"Message from {self.sender.username} in {self.chat_room.name}"