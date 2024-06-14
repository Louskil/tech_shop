from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

# Усі можливі посилання до апі, ендпоінти, приклади використання усіх ендпоінтів можна побачити у post коллекції
urlpatterns = [
    path('', include(router.urls)),
    path('orders/<int:pk>/process/', OrderViewSet.as_view({'post': 'process'}), name='order-process'),
    path('orders/<int:pk>/complete/', OrderViewSet.as_view({'post': 'complete'}), name='order-complete'),
    path('orders/<int:pk>/pay/', OrderViewSet.as_view({'post': 'pay'}), name='order-pay'),
    path('orders/<int:pk>/invoice/', OrderViewSet.as_view({'get': 'invoice'}), name='order-invoice'),
]