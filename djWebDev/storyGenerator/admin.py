from django.contrib import admin
from .models import BlankStory,Genre,WordSet
# Register your models here.


admin.site.register(Genre)
admin.site.register(BlankStory)
admin.site.register(WordSet)

