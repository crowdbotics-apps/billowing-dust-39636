from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AuditLogViewSet,BookingsViewSet,ContentViewSet,EventsViewSet,NotificationViewSet,PaymentMethodViewSet,PaymentsViewSet,TicketsViewSet,UserTypeViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('usertype', UserTypeViewSet )
router.register('content', ContentViewSet )
router.register('events', EventsViewSet )
router.register('notification', NotificationViewSet )
router.register('auditlog', AuditLogViewSet )
router.register('bookings', BookingsViewSet )
router.register('paymentmethod', PaymentMethodViewSet )
router.register('tickets', TicketsViewSet )
router.register('payments', PaymentsViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
