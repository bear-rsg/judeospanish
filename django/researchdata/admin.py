from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Grammars of Judeo-Spanish: Admin Dashboard'


class LanguageAdminView(admin.ModelAdmin):
    list_display = ('name', 'admin_notes')
    search_fields = ('name', 'admin_notes')
    ordering = ('name',)


class LocationAdminView(admin.ModelAdmin):
    list_display = ('name', 'longitude', 'latitude', 'admin_notes')
    search_fields = ('name', 'longitude', 'latitude', 'admin_notes')
    ordering = ('name',)


class StoryAdminView(admin.ModelAdmin):
    list_display = ('description', 'image', 'video_url', 'location', 'location_other', 'knowledge_of_judeospanish')
    search_fields = ('description', 'video_url', 'location_other')
    ordering = ('-id',)


admin.site.register(models.Language, LanguageAdminView)
admin.site.register(models.Location, LocationAdminView)
admin.site.register(models.Story, StoryAdminView)
