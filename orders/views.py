from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

# Функціонал звертання до даних за /api, використовуючи ендпоінти

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'created_at': ['gte', 'lte'],
    }

    @action(detail=True, methods=['post'])
    def process(self, request, pk=None):
        order = self.get_object()
        order.status = 'processed'
        order.save()
        return Response({'status': 'processed'})

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        order = self.get_object()
        order.status = 'completed'
        order.save()
        return Response({'status': 'completed'})

    @action(detail=True, methods=['post'])
    def pay(self, request, pk=None):
        order = self.get_object()
        order.status = 'paid'
        order.save()
        return Response({'status': 'paid'})

    @action(detail=True, methods=['get'])
    def invoice(self, request, pk=None):
        order = self.get_object()
        invoice = order.generate_invoice()
        return Response(invoice)



