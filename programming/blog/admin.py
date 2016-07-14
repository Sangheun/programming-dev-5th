from django.contrib import admin
from blog.models import Post, Blog, Author, Entry

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

admin.site.register(Post, PostAdmin)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)