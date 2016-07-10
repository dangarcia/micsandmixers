from django.contrib import admin

from .models import Show, Stage, Venue

# Register your models here.
admin.site.register(Show)
admin.site.register(Stage)
admin.site.register(Venue)