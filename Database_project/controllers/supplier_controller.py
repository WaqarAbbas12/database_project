from models.supplier import supplier


class SupplierController:
    def __init__(self):
        self.model = supplier()

    def create_supplier(self, name, contact, address):
        self.model.add_supplier(name, contact, address)

    def list_suppliers(self):
        return self.model.get_supplier()
