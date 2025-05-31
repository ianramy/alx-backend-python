from django.db import models
from django.contrib.auth.models import AbstractUser


# Extend the built-in User
class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)


class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        Conversation, related_name="messages", on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
