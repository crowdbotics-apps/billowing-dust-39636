from django.contrib import admin
from .models import AuditLog,Bookings,Content,Events,Notification,UserType
admin.site.register(Notification)
admin.site.register(AuditLog)
admin.site.register(UserType)
admin.site.register(Bookings)
admin.site.register(Content)
admin.site.register(Events)

# Register your models here.
