from django.contrib import admin

from comment.models import Comment


# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'info_hotelcatalog_id', 'created_at')