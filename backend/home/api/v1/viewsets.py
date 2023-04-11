from rest_framework import viewsets
from home.models import Analytics,AuditLog,Bookings,Content,Events,Groups,Notification,PaymentMethod,Payments,Permissions,Roles,Settings,Tickets,UserType
from .serializers import AnalyticsSerializer,AuditLogSerializer,BookingsSerializer,ContentSerializer,EventsSerializer,GroupsSerializer,NotificationSerializer,PaymentMethodSerializer,PaymentsSerializer,PermissionsSerializer,RolesSerializer,SettingsSerializer,TicketsSerializer,UserTypeSerializer
from rest_framework import authentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Notification.objects.all()

class AuditLogViewSet(viewsets.ModelViewSet):
    serializer_class = AuditLogSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = AuditLog.objects.all()

class UserTypeViewSet(viewsets.ModelViewSet):
    serializer_class = UserTypeSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = UserType.objects.all()

class BookingsViewSet(viewsets.ModelViewSet):
    serializer_class = BookingsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Bookings.objects.all()

class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Content.objects.all()

class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Events.objects.all()

class PaymentMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = PaymentMethod.objects.all()

class TicketsViewSet(viewsets.ModelViewSet):
    serializer_class = TicketsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Tickets.objects.all()

class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Payments.objects.all()

class AnalyticsViewSet(viewsets.ModelViewSet):
    serializer_class = AnalyticsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Analytics.objects.all()

class GroupsViewSet(viewsets.ModelViewSet):
    serializer_class = GroupsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Groups.objects.all()

class SettingsViewSet(viewsets.ModelViewSet):
    serializer_class = SettingsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Settings.objects.all()

class RolesViewSet(viewsets.ModelViewSet):
    serializer_class = RolesSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Roles.objects.all()

class PermissionsViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Permissions.objects.all()
