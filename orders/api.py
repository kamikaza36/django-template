from orders.models import Order, Machine, Client
from rest_framework import viewsets, permissions
from django_filters import rest_framework
from .serializers import OrderSerializer, MachineSerializer, ClientSerializer
from .filters import OrderFilter

# Order Viewset
class OrderViewSet(viewsets.ModelViewSet):
    ## queryset = Order.objects.select_related('machine')
    filter_backends = (rest_framework.DjangoFilterBackend,)
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    permissions_classes = [
        permissions.AllowAny
    ]
    def get_queryset(self):
        b = Order.objects.prefetch_related('machine', 'client')
        return b.select_related('machine')

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