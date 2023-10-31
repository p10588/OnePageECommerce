from db.product_repo_postgres import ProductRepo_Postgres

class product_service:

    product_repo = ProductRepo_Postgres
    def GetAllProducts(self):
        self.product_repo.get_all_products()
        pass
