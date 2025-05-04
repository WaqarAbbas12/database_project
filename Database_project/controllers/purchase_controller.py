from models.purchase import purchase


class PurchaseController:
    def __init__(self):
        self.model = purchase()

    def create_purchase(
        self, purchase_id, product_id, supplier_id, quantity, purchase_date
    ):
        self.model.add_purchase(
            purchase_id, product_id, supplier_id, quantity, purchase_date
        )

    def list_purchases(self):
        return self.model.get_purchase()
