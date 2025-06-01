from rest_framework import status # noqa
from django_filters import rest_framework as filters
from rest_framework import viewsets, filters as drf_filters
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.DjangoFilterBackend, drf_filters.OrderingFilter]
    filterset_fields = ["conversation"]
    ordering_fields = ["timestamp"]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
