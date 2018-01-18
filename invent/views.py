from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_tables2 import RequestConfig
from django.views.generic import TemplateView # Import TemplateView
from .models import InventoryParts, Units
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
def inventory_parts_form(request, id=0):
    if request.method=='POST':
        form = InventoryPart(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if id != 0:
                obj = InventoryParts.objects.get(pk=id)
            else:
                obj = InventoryParts()
            obj.description = data['description']
            obj.notes = data['notes']
            obj.unit = Units.objects.get(pk=int(data['unit']))
            obj.active = data['active']
            obj.save()
            #obj.objects.filter(pk=id).update(description=form('description'))
            print ('zapisano')
            return redirect ('/parts/')
    if id!=0:
        part = InventoryParts.objects.get(id=id)
        print (part.part_no)
        form = InventoryPart(initial=dict(part_no=part.part_no, description=part.description, notes=part.note,unit=part.unit.id, active=part.active))
    else:
        form = InventoryPart()
    
    return render(request,'form.html',{'form':form})