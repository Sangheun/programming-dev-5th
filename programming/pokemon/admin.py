from django.contrib import admin

from pokemon.models import Show

class ShowAdmin(admin.ModelAdmin):
    list_display = ('person', 'pokemon', 'place')


admin.site.register(Show, ShowAdmin)