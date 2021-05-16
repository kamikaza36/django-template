import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    machine_name = django_filters.CharFilter()

    machine = django_filters.NumberFilter()
    client = django_filters.NumberFilter()

    order_start_date = django_filters.DateTimeFromToRangeFilter()
    order_end_date = django_filters.DateTimeFromToRangeFilter()

    order_quantity = django_filters.NumberFilter()
    class Meta:
        model = Order
        fields = {
            'order_start_date': ['exact', 'gte', 'lte']
        }
        # fields = {
        #     'started__gte': ['orders__order_start_date__gte'],
        #     'started__lte': ['orders__order_start_date__lte'],
        # }