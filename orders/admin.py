from django.contrib import admin
from .models import Product, Order

# Register your models here.
# Зареєстрував моделі для відображення в адмін панелі.

admin.site.register(Order)
admin.site.register(Product)
