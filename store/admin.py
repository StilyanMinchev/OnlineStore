from django.contrib import admin

from store.models import Watch, Like


class LikeInline(admin.TabularInline):
    model = Like


class WatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = 'price'
    inlines = (
        LikeInline,
    )


admin.site.register(Watch)
admin.site.register(Like)
