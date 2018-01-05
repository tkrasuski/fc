from django.contrib import admin

# Register your models here.
from .models import InventoryParts, Units, InventLocations, InventTransactions, InventHistory
admin.site.register(InventoryParts)
admin.site.register(Units)
admin.site.register(InventLocations)
admin.site.register(InventTransactions)
admin.site.register(InventHistory)