from models.invoice_detail import invoice_detail


class InvoiceDetailController:
    def __init__(self):
        self.model = invoice_detail()

    def create_invoice_detail(
        self, invoice_detail_id, invoice_id, product_id, quantity, price
    ):
        self.model.add_Invoice_detail(
            invoice_detail_id, invoice_id, product_id, quantity, price
        )

    def list_invoice_details(self):
        return self.model.get_invoice_detail()
