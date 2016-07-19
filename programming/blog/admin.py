from django.contrib import admin
from blog.models import Post, Blog, Author, Entry, Person, Group, Membership

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

admin.site.register(Post, PostAdmin)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)

