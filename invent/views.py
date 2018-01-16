from django.shortcuts import render
from django.http import HttpResponse
from django_tables2 import RequestConfig
from django.views.generic import TemplateView # Import TemplateView
from .models import InventoryParts
from .forms import InventoryPart
from .tables import InventoryPartsTable
 

def index(request):
    return render(request, 'dashboard.html')

def about(request):
    return render(request, 'test.html',{'nazwa':'dupa'})
def get_name(request):
    if request.method == 'POST':
        form = InventoryPart(request.POST)
        if form.is_valid():
            print ('OK')
            #print (form.cleaned_data['your_name'])
        else:
            print ('invalid :(')

    else:
        form = InventoryPart()
    return render(request, 'form.html', {'form':form, 'handler': 'inventory_part'})
def inventory_parts_table(request):
    tbl = InventoryPartsTable(InventoryParts.objects.all())
    RequestConfig(request).configure(tbl)
    return render(request, 'table.html', {'tbl':tbl})