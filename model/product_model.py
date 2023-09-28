from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    product_id : int
    product_name : str
    product_description : str
    price : int
    sales_price : int
    image_url : str

@dataclass(frozen=True)
class Product_Spec:
    product_spec_id : str
    product_id : int
    spec_name : str
    spec_detail : str
    

@dataclass(frozen= True)
class Product_Spec_Detail:
    product_spec : str
    product_id : int
    spec_price : int 
    spec_sales_price : int
    spec_image : str
    sku : str

    
