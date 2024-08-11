



class ShoppingItem:
    def __init__(self, id=None, item_name=None, quantity=None, price=None, store_name=None, purchase_date=None):
        self.id = id
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.store_name = store_name
        self.purchase_date = purchase_date
    
   
        
    
    def __str__(self):
        return (f"ShoppingItem(id={self.id}, item_name='{self.item_name}', "
                f"quantity={self.quantity}, price={self.price}, "
                f"store_name='{self.store_name}', purchase_date='{self.purchase_date}')")