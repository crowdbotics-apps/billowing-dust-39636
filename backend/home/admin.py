from django.contrib import admin
from .models import Analytics,AuditLog,Bookings,Content,Events,Groups,Notification,PaymentMethod,Payments,Permissions,Roles,Settings,Tickets,UserType
admin.site.register(Notification)
admin.site.register(AuditLog)
admin.site.register(UserType)
admin.site.register(Bookings)
admin.site.register(Content)
admin.site.register(Events)
admin.site.register(PaymentMethod)
admin.site.register(Tickets)
admin.site.register(Payments)
admin.site.register(Analytics)
admin.site.register(Groups)
admin.site.register(Settings)
admin.site.register(Roles)
admin.site.register(Permissions)

# Register your models here.
