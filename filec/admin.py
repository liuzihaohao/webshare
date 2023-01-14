from django.contrib import admin
from .models import filed
# Register your models here.

class filedAdmin(admin.ModelAdmin):
	list_display = ['id','name','duuid','filedf','ctime']
	list_display_links = ['id']
	search_fields = ['name','duuid','ctime']

admin.site.register(filed,filedAdmin)

admin.site.site_title="File share"
admin.site.site_header="File share"


from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session

class LogEntryAdmin(admin.ModelAdmin):
	list_display = ['action_time','user','content_type','object_id','object_repr','action_flag','change_message']

admin.site.register(LogEntry,LogEntryAdmin)

class SessionAdmin(admin.ModelAdmin):
	list_display = ['session_key','session_data','expire_date']

admin.site.register(Session,SessionAdmin)