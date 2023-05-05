from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.dispatch import receiver

from mesages.mixins import (
    ResponseMixin,
    ObjectMixin,
)
from mesages.models import (
    Message,
    Chat,
    User
)
from mesages.serializers import (
    MessageSerializer,
    ChatSerializer,
    UserSerializer
)


class MessageViewSet(ResponseMixin, ObjectMixin, ViewSet):
    """ViewSet about chats and messages."""

    queryset: QuerySet[Message] = \
        Message.objects.select_related('to_send').all()

    # list of all
    def list(self, request: Request, *args: Any) -> Response:
        """GET method."""

        serializer: MessageSerializer = MessageSerializer(
            self.queryset, many=True
        )

        return Response(
            data=serializer.data
        )

    # retrieve only one message
    def retrieve(self, request: Request, pk: int, *args: tuple) -> Response:
        """GET method to retrieve a single message by ID."""

        message: Message = get_object_or_404(self.queryset, pk=pk)
        serializer: MessageSerializer = MessageSerializer(message)

        return Response(
            data=serializer.data
        )
