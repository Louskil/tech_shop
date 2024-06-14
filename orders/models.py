from django.db import models
from django.utils import timezone
from datetime import timedelta

# Моделі товарів та замовлень для бази даних
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def discount_price(self):
        if timezone.now() - self.created_at > timedelta(days=30):
            return float(str(self.price)) * float('0.8')  # 20% знижка
        return self.price

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('processed', 'Processed'),
        ('completed', 'Completed'),
        ('paid', 'Paid'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_invoice(self):
        invoice_data = {
            "order_id": self.id,
            "product_name": self.product.name,
            "product_price": self.product.discount_price,
            "order_date": self.created_at,
            "invoice_date": timezone.now()
        }
        return invoice_data

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"
