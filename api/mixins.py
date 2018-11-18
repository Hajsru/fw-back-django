from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import CommentSerializer

# Custom схема для генерации документации метода comment
comment_response = openapi.Response('Объект комментария', CommentSerializer)
comment_schema = {
    'method': 'post',
    'request_body': CommentSerializer,
    'responses': {200: comment_response},
    'operation_description': 'Комментирование объекта'
}


# pylint: disable=too-few-public-methods; mixin с одним методом
class CommentedObjectMixin:
    """
    Mixin добавляющий возможность прокомментировать объект через POST запрос на
    /object/{pk}/comment
    Содержит в себе custom схему для генерации документации api

    """

    @swagger_auto_schema(**comment_schema)
    @action(methods=['post'], detail=True)
    def comment(self, request, pk):
        obj = self.get_object()
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            comment = serializer.save()
            obj.comments.add(comment)
            obj.save()
            return Response(CommentSerializer(comment).data)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
