from config.config import ConnectDB, load_envs

db_name, username, host, password = load_envs()


class purchase:
    def __init__(self):
        self.DB = ConnectDB(db_name, username, host, password)
        self.conn, self.curr = self.DB.connect_db()

    def add_supplier(
        self, purchase_id, product_id, supplier_id, quantity, purchase_date
    ):
        query = "INSERT INTO Purchases (purchase_id ,product_id, supplier_id, quantity, purchase_date) VALUES (%s, %s, %s, %s, %s)"
        self.curr.execute(
            query, (purchase_id, product_id, supplier_id, quantity, purchase_date)
        )
        self.conn.commit()

    def get_purchase(self):
        query = "SELECT * FROM Purchases"
        self.curr.execute(query)
        results = self.curr.fetchall()
        print("All Purchases:")
        for i, purchase in enumerate(results):
            print(
                f"\nPurchase No: {i+1}\nPurchase ID: {purchase[0]}\nProduct ID: {purchase[1]}\nSupplier ID: {purchase[2]}\nQuantity: {purchase[3]}"
            )
