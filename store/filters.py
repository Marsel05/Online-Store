from .models import *
from django_filters.rest_framework import FilterSet

class OrderItemFilter(FilterSet):
    class Meta:
        model = OrderItem
        fields = {
            'price': ['gt', 'lt'],

        }