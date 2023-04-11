from django.contrib import admin
from .models import AuditLog,Bookings,Content,Events,Notification,PaymentMethod,Payments,Tickets,UserType
admin.site.register(Notification)
admin.site.register(AuditLog)
admin.site.register(UserType)
admin.site.register(Bookings)
admin.site.register(Content)
admin.site.register(Events)
admin.site.register(PaymentMethod)
admin.site.register(Tickets)
admin.site.register(Payments)

# Register your models here.
