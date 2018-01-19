from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_tables2 import RequestConfig
from django.views.generic import TemplateView # Import TemplateView
from .models import InventoryParts, Units, Customer, DeliveryAddress
from .forms import InventoryPart, CustomerForm, DeliveryAddressForm
from .tables import InventoryPartsTable, CustomerOverviewTable, CustomerDeliveryAddressesTable
from .inventoryTransactions import InventTransaction as IT

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
    return render(request, 'table.html', {'tbl':tbl,'site_name':'Inventory parts overview'})
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
def customer_overview_table(request):
    tbl = CustomerOverviewTable(Customer.objects.all())
    RequestConfig(request).configure(tbl)
    return render(request, 'table.html', {'tbl':tbl, 'site_name':'Customer overview'})
    
def customer_form(request, id=0):
    if id != 0:
        customer = Customer.objects.get(id=id)
        form = CustomerForm(initial=dict(name=customer.name, vat_no=customer.vat_no, address1=customer.address1, address2=customer.address2, phone1=customer.phone1, phone2=customer.phone2, email=customer.email, notes=customer.notes))
    else:
        form=CustomerForm()
    return render(request,'form.html',{'form':form})
def customer_delivery_addresses_table(request):
    tbl = CustomerDeliveryAddressesTable(DeliveryAddress.objects.all())
    RequestConfig(request).configure(tbl)
    return render(request, 'table.html', {'tbl':tbl, 'site_name':'Delivery address overview'})
def customer_delivery_addresses_form(request, id=0):
    if request.method == 'POST':
        form = DeliveryAddressForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if id != 0:
                obj = DeliveryAddress.objects.get(pk=id)
            else:
                obj = DeliveryAddress()
            obj.customer = Customer.objects.get(pk=data['customer'])
            obj.description = data['description']
            obj.address = data['address']
            obj.phone = data['phone']
            obj.email = data['email']
            obj.save()
    if id != 0:
        address = DeliveryAddress.objects.get(id=id)
        form = DeliveryAddressForm(initial=dict(customer=address.customer.id, description=address.description, address=address.address, phone=address.phone, email=address.email))
    else:
        form = DeliveryAddressForm()
    return render(request,'form.html',{'form':form, 'site_name':'Customer delivery address'})

def test_test(request):
    it = IT()
    it.part_no = 'test_002'
    it.qty = 1
    it.source_location = 'default'
    it.dest_location = 'testo'
    it.move()
    return render(request, 'test.html',{'nazwa':it.t})