from braces.views import SelectRelatedMixin
from django.contrib import admin

from . import models

class PostAdmin(admin.ModelAdmin):
    fields = ['group', 'user', 'message']
    search_fields = ['message', 'user__username', 'group__name']
    list_filter = ['group', 'user', 'message']
    list_display = ['group', 'user', 'message']



admin.site.register(models.Post, PostAdmin)

