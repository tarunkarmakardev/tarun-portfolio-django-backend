from django.contrib import admin
from .models import Skill, Project, Resume, Endpoint, TextSection

# Register your models here.


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'icon_html')
    list_display_links = ('skill_name', 'icon_html')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'proj_url', 'github_url')
    list_display_links = ('title', 'proj_url', 'github_url')
    list_filter = ('title', 'proj_url', 'github_url')
    search_fields = ['description', 'title']


@admin.register(Resume)
class Resume(admin.ModelAdmin):
    list_display = ('date',)
    readonly_fields = ('date',)


@admin.register(Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    list_display_links = ('title', 'url',)


@admin.register(TextSection)
class EndpointAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail',)
    list_display_links = ('title', 'detail',)
