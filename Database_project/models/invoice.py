from config.config import ConnectDB, load_envs

db_name, username, host, password = load_envs()


class invoice:
    def __init__(self):
        self.DB = ConnectDB(db_name, username, host, password)
        self.conn, self.curr = self.DB.connect_db()

    def add_invoice(self, invoice_id, customer_id, invoice_date):
        query = "INSERT INTO Invoices (invoice_id, customer_id, invoice_date) VALUES (%s, %s, %s)"
        self.curr.execute(query, (invoice_id, customer_id, invoice_date))
        self.conn.commit()

    def get_invoice(self, invoice_id):
        query = "SELECT * FROM Invoices WHERE invoice_id = %s"
        self.curr.execute(query, (invoice_id,))
        results = self.curr.fetchall()
        print(f"Details for Invoice ID: {invoice_id}")
        for i, invoice in enumerate(results):
            print(
                f"\nInvoice No: {invoice[0]}\nInvoice ID: {invoice[0]}\nCustomer ID: {invoice[1]}\nDate: {invoice[2]}"
            )
