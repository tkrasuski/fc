import django_tables2 as tables
from .models import InventoryParts, Customer, DeliveryAddress
from django.utils.safestring import mark_safe, SafeText

class InventoryPartsTable(tables.Table):
    def render_part_no(self,value, record):
        #url = record.id
        url = '/parts/details/'+str(record.id)+'/'
        return mark_safe('<a href="%s">%s</a>' % (url, record.part_no))

    class Meta:
        model = InventoryParts
        template = 'django_tables2/bootstrap.html'
        exclude = ('id', 'note')
class PartsInStock(tables.Table):
    def render_part_no(self, value, record):
        pass

class InventoryTransations(tables.Table):
    pass
class CustomerOrders(tables.Table):
    pass
class InventoryLocations(tables.Table):
    pass
class InventoryHistory(tables.Table):
    pass

class CustomerOverviewTable(tables.Table):
    def render_name(self, value, record):
        url = '/customer/details/'+str(record.id)+'/'
        return mark_safe('<a href="%s">%s</a>' % (url, record.name))
    class Meta:
        model = Customer
        template = 'django_tables2/bootstrap.html'
        exclude = ('id', 'note')

class CustomerDeliveryAddressesTable(tables.Table):
    def render_customer(self, value, record):
        url = '/customer/address_details/'+str(record.id)+'/'
        return mark_safe('<a href="%s">%s</a>' % (url, record.customer))
    class Meta:
        model = DeliveryAddress
        template = 'django_tables2/bootstrap.html'
        exclude = ('id')