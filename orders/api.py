from orders.models import Order, Machine, Client
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer, MachineSerializer, ClientSerializer

# Order Viewset
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = MachineSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClientSerializer