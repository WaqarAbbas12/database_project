from config.config import ConnectDB, load_envs

db_name, username, host, password = load_envs()


class invoice_detail:
    def __init__(self):
        self.DB = ConnectDB(db_name, username, host, password)
        self.conn, self.curr = self.DB.connect_db()

    def add_Invoice_detail(
        self, invoice_detail_id, invoice_id, product_id, quantity, price
    ):
        query = "INSERT INTO invoice_details (invoice_detail_id, invoice_id, product_id, quantity, price) VALUES (%s, %s, %s, %s, %s)"
        self.curr.execute(
            query, (invoice_detail_id, invoice_id, product_id, quantity, price)
        )
        self.conn.commit()

    def get_invoice_detail(self):
        query = "SELECT * FROM invoice_details"
        self.curr.execute(query)
        results = self.curr.fetchall()
        print("All Invoices:")
        for i, result in enumerate(results):
            print(
                f"\nInvoice No:{i+1}\nInvoice Detail Id:{result[0]}\nProduct Id:{result[2]}\nQuantity:{result[3]}\nPrice:{result[4]}"
            )
