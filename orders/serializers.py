from rest_framework import serializers, fields
from orders.models import Order, Machine, Client

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    order_start_date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'])
    order_end_date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'])

    class Meta:
        model = Order
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'