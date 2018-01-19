from .models import InventoryParts, InventLocations, InventTransactions, InventHistory, PartsInStock


class InventTransaction():
    part_no = None
    source_location = None
    dest_location = None
    qty = None
    error = None
    t=None
    def move(self):
        self.error = None
        if self.part_no and self.source_location and self.dest_location and self.qty:
            # checking if qty of part in stock is sufficient for transaction
            part = InventoryParts.objects.get(part_no=self.part_no)
            slocation = InventLocations.objects.get(location_code = self.source_location)
            aval = PartsInStock.objects.get(part_no=part, location=slocation)
            aval_qty = aval.quantity
            if aval_qty < self.qty:
                print ('too few parts to move')
                self.error = 'too few parts to move'
            else:
                # chceck whether destination location exists
                dlocation = InventLocations.objects.get(location_code=self.dest_location)

                # decrease source
                aval.quantity=aval.quantity-self.qty
                aval.save()
                # put here insert to trans hist
                # increase dest or insert record
                daval, created = PartsInStock.objects.update_or_create(part_no = part, location=dlocation)
                # put here insert to trans hist
                if created:
                    daval.part_no = part
                    daval.location=dlocation
                    daval.quantity = self.qty
                    daval.save()
                else:
                    daval.location = dlocation
                    daval.quantity = daval.quantity + self.qty
                    daval.save()
                    print (daval.location)
                self.t = dlocation
            
        else:
            print ('no parameters')