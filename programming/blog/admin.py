from django.contrib import admin
from blog.models import Post, Blog, Author, Entry, Person, Group, Membership, Contact, Tag, ZipCode, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']


class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'city', 'gu', 'dong', 'road']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'message','author']


admin.site.register(Post, PostAdmin)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Contact)

admin.site.register(ZipCode, ZipCodeAdmin)

admin.site.register(Comment, CommentAdmin)