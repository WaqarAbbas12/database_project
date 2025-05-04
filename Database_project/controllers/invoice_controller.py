from models.invoice import invoice


class InvoiceController:
    def __init__(self):
        self.model = invoice()

    def create_invoice(self, invoice_id, customer_id, invoice_date):
        self.model.add_invoice(invoice_id, customer_id, invoice_date)

    def list_invoice(self, invoice_id):
        return self.model.get_invoice(invoice_id)
