from django.db import models

# Create your models here.

class Units(models.Model):
    code = models.CharField(max_length=5, null=False)
    description = models.CharField(max_length=100, null=False)
    notes = models.CharField(max_length=2000)
    stamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.description
    
class InventoryParts(models.Model):
    part_no = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)
    note = models.TextField()
    unit = models.ForeignKey('Units', on_delete=models.CASCADE)
    active = models.BooleanField(null=False)
    stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.description

class InventTransactions(models.Model):
    direction_choice = (('+','Plus'),('-','Minus'),('0','Zero'), ('+v','IncrValue'), ('-v','DecrValue'))
    transaction_code = models.CharField(max_length=10)
    transaction_type = models.CharField(max_length=10)
    transaction_direction = models.CharField(max_length=2, choices=direction_choice, null=True)
    stamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.transaction_code
    

class InventLocations(models.Model):
    type_choice=(('Int','Internal'),('Ext','External'))
    location_code = models.CharField(max_length=10, null=False)
    location_name = models.CharField(max_length=100)
    location_type = models.CharField(max_length=30, choices=type_choice, null=True)
 #   bay = models.CharField(max_length=10)
    note = models.TextField()
    active = models.BooleanField(null=False)
    stamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.location_code
class LocationBay(models.Model):
    location = models.ForeignKey('InventLocations',on_delete=models.CASCADE, default=None)
    bay = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.location.location_code + ' / ' + self.bay

class InventHistory(models.Model):
    transaction_code = models.ForeignKey('InventTransactions', on_delete=models.CASCADE)
    part_no =  models.ForeignKey('InventoryParts', on_delete=models.CASCADE, null=True)
    source_location = models.CharField(max_length=10, null=False)
    destination_location = models.CharField(max_length=10, null=False)
    quantity = models.FloatField(null=False)
    value = models.FloatField(null=False)
    stamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.transaction_code
class PartsInStock(models.Model):
    part_no = models.ForeignKey('InventoryParts', on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey('InventLocations', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.FloatField(null=True)
    value = models.FloatField(null=True)
    batch = models.CharField(max_length=30,null=True, blank=True)
    stamp = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    def __str__(self):
        return self.part_no.part_no+'/'+self.location.location_code
class Customer(models.Model):
    name = models.CharField(max_length=100, null=False)
    vat_no = models.CharField(max_length=30, null=True)
    address1 = models.TextField()
    address2 = models.TextField()
    phone1 = models.CharField(max_length=10, null=True, blank=True)
    phone2 = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    notes = models.TextField()
    stamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name
class DeliveryAddress(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=False)
    address = models.TextField()
    phone = models.CharField(max_length=30,null=True, blank=True)
    email = models.EmailField(blank=True)
    stamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.customer.name + ' ' + self.description
class CustomerOrderHead(models.Model):
    pass
    #customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
