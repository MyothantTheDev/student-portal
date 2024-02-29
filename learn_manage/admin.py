from django.contrib import admin
from .models import Answer,Grade,Question,NoticeBoard
# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user','question']
    search_fields = ['user__id','user__name']

admin.site.register(Answer,AnswerAdmin)
admin.site.register(Grade)
admin.site.register(Question)
admin.site.register(NoticeBoard)