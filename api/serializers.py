from rest_framework import serializers

from .models import Speaker, Presentation, Event, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('content_type', 'object_id',)


class ObjectWithCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    @staticmethod
    def get_comments(obj):
        """
        Метод используется для получения списка комментариев объекта
        с помощью фильтрации комментариев относящихся к данному объекту
        :param obj: комментируемый объект
        :return: список комментариев объекта

        """

        qs = Comment.objects.filter(object_id=obj.id)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data


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
