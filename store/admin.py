from django.contrib import admin

from store.models import Watch, Like, Comment


class LikeInline(admin.TabularInline):
    model = Like


class WatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = 'price'
    inlines = (
        LikeInline,
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'watch_id')


admin.site.register(Watch)
admin.site.register(Like)
admin.site.register(Comment)
