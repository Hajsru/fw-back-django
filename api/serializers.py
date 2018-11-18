from rest_framework import serializers

from .models import Speaker, Presentation, Event, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ObjectWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)


class EventSerializer(ObjectWithCommentsSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class PresentationSerializer(ObjectWithCommentsSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'


class SpeakerSerializer(ObjectWithCommentsSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'
