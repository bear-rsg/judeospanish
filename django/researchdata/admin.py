from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Linguistic Atlas of Judeo-Spanishes: Admin Dashboard'


def admin_publish_selected(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to published
    """
    queryset.update(admin_published=True)


admin_publish_selected.short_description = "Publish selected items (will appear on public site)"


def admin_unpublish_selected(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not published
    """
    queryset.update(admin_published=False)


admin_unpublish_selected.short_description = "Unpublish selected items (will not appear on public site)"


class LanguageAdminView(admin.ModelAdmin):
    list_display = ('name', 'admin_notes')
    search_fields = ('name', 'admin_notes')
    ordering = ('name',)


class LocationAdminView(admin.ModelAdmin):
    list_display = ('name', 'longitude', 'latitude', 'admin_notes')
    search_fields = ('name', 'longitude', 'latitude', 'admin_notes')
    ordering = ('name',)


class StoryAdminView(admin.ModelAdmin):
    list_display = ('description_short', 'image', 'video_url', 'location',
                    'location_other', 'knowledge_of_judeospanish', 'admin_published')
    search_fields = ('description', 'video_url', 'location_other')
    ordering = ('-id',)
    list_filter = ('admin_published',)
    readonly_fields = ('meta_created_datetime', 'meta_lastupdated_datetime')
    actions = (admin_publish_selected, admin_unpublish_selected)


class ParticipationActivityAdminView(admin.ModelAdmin):
    list_display = ('name', 'admin_notes')
    search_fields = ('name', 'admin_notes')
    ordering = ('name',)


class ParticipantAdminView(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'emai', 'admin_notes')
    ordering = ('name',)


admin.site.register(models.Language, LanguageAdminView)
admin.site.register(models.Location, LocationAdminView)
admin.site.register(models.Story, StoryAdminView)
admin.site.register(models.ParticipationActivity, ParticipationActivityAdminView)
admin.site.register(models.Participant, ParticipantAdminView)
