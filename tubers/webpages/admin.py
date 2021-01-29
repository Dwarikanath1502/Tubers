from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width = "40px" />'.format(object.photo.url))
    
    list_display = ('id','myphoto', 'first_name', 'role', 'created_date')     #now in admin panel it show more detailed section
    list_display_links = ('first_name', 'id')   # if alone put , here because list cna't be without key but it doesn't have
    search_fields = ('first_name', 'role')  #activating search field
    list_filter = ('role',) #enabling filter

admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)