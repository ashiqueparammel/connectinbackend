from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from users.models import CustomUser
from users.serializers import userDataSerializer
from .models import Message

class MessageSerializer(ModelSerializer):
    sender_email=serializers.EmailField(source='sender.email')

    class Meta:
        model=Message
        fields=['message','sender_email','timestamp']