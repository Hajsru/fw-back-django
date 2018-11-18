from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .mixins import CommentedObjectMixin
from .models import Event, Comment, Speaker, Presentation
from .serializers import EventSerializer, CommentSerializer, \
    PresentationSerializer, SpeakerSerializer


class EventViewSet(CommentedObjectMixin, ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    pagination_class = None


class PresentationViewSet(CommentedObjectMixin,
                          ReadOnlyModelViewSet):
    serializer_class = PresentationSerializer
    queryset = Presentation.objects.all()
    pagination_class = None


class SpeakerViewSet(CommentedObjectMixin, ReadOnlyModelViewSet):
    serializer_class = SpeakerSerializer
    queryset = Speaker.objects.all()
    pagination_class = None


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = None
