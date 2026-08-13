from django.contrib import admin
from app1.models import hostel

class hostel_admin(admin.ModelAdmin):
    list_display=['name','pin','fee']
admin.site.register(hostel,hostel_admin)

# Register your models here.
