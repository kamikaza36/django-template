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
    order_start_date = serializers.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'])
    order_end_date = serializers.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'])

    client_id = serializers.IntegerField()
    machine_id = serializers.IntegerField()

    machine = MachineSerializer()
    client = ClientSerializer()
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        machine_data = validated_data.pop('machine')
        client_data = validated_data.pop('client')
        print(type(validated_data))
        if machine_data:
            Machine.objects.create(**machine_data)
        if client_data:
         Client.objects.create(**client_data)
        order = Order.objects.create(**validated_data)
        return order

