from rest_framework import serializers
from .models import ChatRoom, Message

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username', read_only=True)
    sender_type = serializers.CharField(source='sender.user_type', read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'content', 'sender_name', 'sender_type', 'timestamp']

class ChatRoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    building_name = serializers.CharField(source='building.name', read_only=True)
    websocket_url = serializers.SerializerMethodField()

    class Meta:
        model = ChatRoom
        fields = ['id', 'building', 'building_name', 'name', 'messages', 'websocket_url']

    def get_websocket_url(self, obj):
        return f'ws://{self.context["request"].get_host()}/ws/chat/{obj.id}/'