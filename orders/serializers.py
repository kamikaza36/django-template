from rest_framework import serializers, fields
from orders.models import Order, Machine, Client

# Order Serializer

class MachineSerializer(serializers.ModelSerializer):
    machine_name = fields.CharField(max_length=100, allow_blank=True)

    class Meta:
        model = Machine
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(max_length=100, allow_blank=True)
    class Meta:
        model = Client
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_start_date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'])
    order_end_date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'])

    machine = MachineSerializer()
    client = ClientSerializer()
    class Meta:
        model = Order
        fields = '__all__'