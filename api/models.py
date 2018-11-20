from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.timezone import now
from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    modified = models.DateTimeField(auto_now=True, verbose_name='Изменено')

    class Meta:
        abstract = True


class CommentedObjectModel(models.Model):
    comments = GenericRelation('Comment', verbose_name='Комментарии')

    class Meta:
        abstract = True


class Comment(TimeStampedModel):
    comment_text = models.TextField(verbose_name='Комментарий')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     null=True)
    object_id = models.PositiveIntegerField(null=True)
    commented_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return f'Комментарий: {self.comment_text[:50]}'

    @property
    def short_comment(self):
        return self.comment_text if len(
            self.comment_text) < 50 else self.comment_text[:50] + '...'

    short_comment.fget.short_description = 'Комментарий'


# class Rating(BaseModel):
#     rating_value = models.IntegerField(verbose_name='Рейтинг')
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#
#     class Meta:
#         verbose_name = 'рейтинг'
#         verbose_name_plural = 'рейтинги'
#
#     def __str__(self):
#         return f'Рейтинг: {self.rating_value}'


class Event(TimeStampedModel, CommentedObjectModel):
    name = models.TextField(verbose_name='Название события')
    description = models.TextField(blank=True, verbose_name='Описание события')
    event_date = models.DateTimeField(default=now, verbose_name='Дата события')
    place_name = models.TextField(blank=True, verbose_name='Место проведения')
    place_picture = models.TextField(blank=True,
                                     verbose_name='Фото места проведения')
    presentations = models.ManyToManyField('Presentation',
                                           verbose_name='Доклады')

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'

    def __str__(self):
        return f'Событие: {self.name[:50]}'


class Presentation(TimeStampedModel, CommentedObjectModel):
    name = models.TextField(verbose_name='Название доклада')
    description = models.TextField(blank=True, verbose_name='Описание доклада')
    images = ArrayField(models.CharField(max_length=255),
                        verbose_name='Фотографии доклада', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='Спикеры')

    class Meta:
        verbose_name = 'доклад'
        verbose_name_plural = 'доклады'

    def __str__(self):
        return f'Доклад: {self.name[:50]}'


class Speaker(TimeStampedModel, CommentedObjectModel):
    name = models.TextField(verbose_name='Имя спикера')
    photo = models.TextField(blank=True, verbose_name='Фото спикера')
    description = models.TextField(blank=True, verbose_name='Описание спикера')

    class Meta:
        verbose_name = 'спикер'
        verbose_name_plural = 'спикеры'

    def __str__(self):
        return f'Спикер: {self.name}'
