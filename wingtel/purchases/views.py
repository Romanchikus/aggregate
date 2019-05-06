from rest_framework import viewsets

from wingtel.purchases.models import Purchase
from wingtel.purchases.serializers import PurchaseSerializer


class PurchaseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
