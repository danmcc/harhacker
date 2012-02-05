from django.contrib import admin
from harhacker.pollers import models

class Har(admin.ModelAdmin):
    fields = ('user', 'url')
    list_display = ('user', 'url')

admin.site.register(models.Har, Har)
