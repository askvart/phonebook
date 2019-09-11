from django.contrib import admin

from .models import Tt
from .models import Rubric

class TtAdmin(admin.ModelAdmin):
    list_display = ('family', 'content', 'nomer','rubric')
    list_display_links = ('family', 'nomer')
    search_fields = ('family', 'nomer',)

admin.site.register(Tt, TtAdmin)
admin.site.register(Rubric)

