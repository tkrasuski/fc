import django_tables2 as tables
from .models import InventoryParts

class InventoryPartsTable(tables.Table):
    class Meta:
        model = InventoryParts
        template = 'django_tables2/bootstrap.html'