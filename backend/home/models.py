from django.conf import settings
from django.db import models
class Notification(models.Model):
    'Generated Model'
    typeID = models.IntegerField()
    title = models.TextField()
    bodytext = models.TextField()
    datetime = models.DateTimeField()
    status = models.BooleanField()
    duedate = models.DateField()
    datecreated = models.DateTimeField()
    userID = models.ForeignKey("users.User",on_delete=models.CASCADE,null=True,blank=True,related_name="notification_userID",)
class AuditLog(models.Model):
    'Generated Model'
    content = models.BigIntegerField()
    objectID = models.IntegerField()
    datetime = models.DateTimeField()
    recordID = models.IntegerField()
    action = models.TextField()
    userID = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="auditlog_userID",)
class UserType(models.Model):
    'Generated Model'
    full_name = models.TextField()
    email = models.EmailField(max_length=254,)
    status = models.BooleanField()
    mobile = models.IntegerField()
    roleID = models.IntegerField()
    userID = models.ForeignKey("users.User",on_delete=models.CASCADE,null=True,blank=True,related_name="usertype_userID",)
class Bookings(models.Model):
    'Generated Model'
    status = models.IntegerField()
    eventID = models.ForeignKey("home.Events",on_delete=models.CASCADE,related_name="bookings_eventID",)
class Content(models.Model):
    'Generated Model'
    type = models.TextField()
    body = models.TextField()
class Events(models.Model):
    'Generated Model'
    title = models.TextField()
    date = models.DateTimeField()
    state = models.IntegerField()
    address = models.TextField()
    tickets_sold = models.BooleanField()
    ticketID = models.IntegerField()
    event_typeID = models.IntegerField()
