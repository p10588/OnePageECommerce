from dataclasses import dataclass

@dataclass(frozen=True)
class InventoryItem:
    sku : str
    product_name : str
    stock_quantity : int

 

class InventoryService:
    def process_inventory(self, order_items:[], callback, fallback):
        response = order_items # send request to inventory (third party or other service)
        if response :
            if callback: callback()
            print('Send order list success !!')
        else:
            if fallback: fallback()
            print('Send order list fail !!')

    