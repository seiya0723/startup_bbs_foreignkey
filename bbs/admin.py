# == This code was created by https://noauto-nolife.com/post/django-auto-create-models-forms-admin/ == #

from django.contrib import admin
from .models import Category,Topic,Reply

class CategoryAdmin(admin.ModelAdmin):
    list_display	= [ "id", "name" ]

class TopicAdmin(admin.ModelAdmin):
    list_display	= [ "id", "category", "comment" ]

class ReplyAdmin(admin.ModelAdmin):
    list_display	= [ "id", "target", "comment" ]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Reply,ReplyAdmin)
