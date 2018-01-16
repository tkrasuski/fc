import django_tables2 as tables
from .models import InventoryParts
from django.utils.safestring import mark_safe, SafeText

class InventoryPartsTable(tables.Table):
    def render_part_no(self,value, record):
        url = record.id
        return mark_safe('<a href="%s">%s</a>' % (url, record))

    class Meta:
        model = InventoryParts
        template = 'django_tables2/bootstrap.html'
        exclude = ('id', 'note')