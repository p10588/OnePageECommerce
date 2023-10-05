import pytest
from models.product_model import Product
from db.product_repo_postgres import ProductRepo_Postgres  

def test_add_product():
    product = Product(
        product_id=0,
        product_name="Sample Product",
        product_description="This is a sample product description.",
        price=100,
        sales_price=80,
        image_url="https://example.com/sample_product.jpg"
    )

    try:
        productRepo = ProductRepo_Postgres()
        productRepo.add_product(product)
        assert True
    except Exception as e:
        print(f'Error: {e}')
        assert False

def test_update_product():
    try:
        productRepo = ProductRepo_Postgres()
        productRepo.update_product_data(0,'product_name','vvv')
        assert True
    except Exception as e:
        print(f'Error: {e}')
        assert False

def test_get_all_product():
    try:
        productRepo = ProductRepo_Postgres()
        products = productRepo.get_all_products()
        for p in products:
            print(p)
        assert True
    except Exception as e:
        print(f'Error: {e}')
        assert False

def test_get_product():
    try:
        productRepo = ProductRepo_Postgres()
        product = productRepo.get_product(0)
        print(product)
        assert True
    except Exception as e:
        print(f'Error: {e}')
        assert False


def test_import_product_list():
    try: 
        productRepo = ProductRepo_Postgres()
        path = '/Volumes/Chain/Workspaces/OnePageEcommerce/products_202310031617.txt'
        productRepo.import_product_list(path)
        assert True
    except Exception as e:
        print(f'Error: {e}')
        assert False

def remove_product():
    try:
        productRepo = ProductRepo_Postgres()
        productRepo.remove_product(0)
        assert True
    except Exception as e:
        print(f'Error: {e}')
        assert False


  
        