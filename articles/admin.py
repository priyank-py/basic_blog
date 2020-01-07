from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    def body_part(self, instance):
        return instance.body[0:25] + '...'
    list_display = ['id', 'title', 'writer', 'published_on', 'genre', 'modified_on', 'body_part']
    list_display_links = ['id', 'title']
    list_filter = ['genre',]
    search_fields = ['title', 'writer__username']


admin.site.register(Article, ArticleAdmin)

