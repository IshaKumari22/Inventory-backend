from rest_framework import viewsets
from .models import Product,Supplier
from .serializers import ProductSerializer,SupplierSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum,F


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset=Supplier.objects.all()
    serializer_class=SupplierSerializer

@api_view(['GET'])
def stats(request):
    total_products=Product.objects.count()
    total_suppliers=Supplier.objects.count()
    low_stock=Product.objects.filter(quantity__lt=5).count()

    inventory_value=Product.objects.aggregate(
        total_value=Sum(F('price')*F('quantity'))
    )['total_value'] or 0

    return Response({
        "total_products":total_products,
        "total_suppliers":total_suppliers,
        "low_stock":low_stock,
        "inventory_value":inventory_value
    })