from config.config import ConnectDB, load_envs

db_name, username, host, password = load_envs()


class Views:
    def __init__(self):
        self.DB = ConnectDB(db_name, username, host, password)
        self.conn, self.curr = self.DB.connect_db()

    def view_invoice_summary(self):
        query = "SELECT * FROM invoice_summary_view"
        return self.curr.fetchall()

    def view_stock(self):
        query = "SELECT * FROM invoice_summary_view"
        self.curr.execute(query)
        results = self.curr.fetchall()
        print("Invoice Summary View:")
        for i, row in enumerate(results):
            print(
                f"\nRecord No: {i+1}\nInvoice ID: {row[0]}\nProduct ID: {row[1]}\nProduct Name: {row[2]}"
                f"\nQuantity: {row[3]}\nPrice: {row[4]}\nTotal: {row[5]}"
            )
