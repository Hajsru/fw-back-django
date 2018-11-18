from django.contrib import admin

from .models import Event, Presentation, Speaker, Comment


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date',)
    list_filter = ('event_date', 'presentations__speakers__name')
    search_fields = (
        'name', 'description', 'place_name', 'presentations__speakers__name',)


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('speakers__name',)
    search_fields = ('name', 'description', 'speakers__name',)


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', 'description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('short_comment', 'created',)
    list_display_links = ('short_comment',)
    list_filter = ('created',)
    search_fields = ('short_comment',)
