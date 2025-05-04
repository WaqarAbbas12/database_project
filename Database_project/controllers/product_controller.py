from models.product import product


class ProductController:
    def __init__(self):
        self.model = product()

    def create_product(self, product_id, name, category, price, stock_quantity):
        self.model.add_product(product_id, name, category, price, stock_quantity)

    def list_products(self):
        return self.model.get_product()
