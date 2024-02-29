from django.contrib import admin
from .models import Section, Profile, Message

# Register your models here.
admin.site.register(Section)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','image']
    search_fields = ['user__username', 'user__id']
    

admin.site.register(Profile,ProfileAdmin)


admin.site.register(Message)