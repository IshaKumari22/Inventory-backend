from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupplierViewSet,stats
from django.urls import path
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'suppliers', SupplierViewSet, basename='suppliers')

urlpatterns = router.urls +[
    path('stats/',stats),
]
