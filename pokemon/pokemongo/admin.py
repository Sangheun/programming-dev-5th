from django.contrib import admin

from .models import Pokemon, Trainer, CatchInfo

admin.site.register(Pokemon)
admin.site.register(Trainer)
admin.site.register(CatchInfo)