from rest_framework import serializers
from .models import Product, Order


# Серіалізатори для товарів та замовлень, дозволяє системі мати ендпоінти
class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'created_at', 'discount_price']

class OrderSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')

    class Meta:
        model = Order
        fields = ['id', 'product_id', 'status', 'created_at']

    def create(self, validated_data):
        product = validated_data.pop('product')
        order = Order.objects.create(product=product, **validated_data)
        return order