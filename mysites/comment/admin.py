from django.contrib import admin
from comment.models import Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_object','text','comment_time','user')