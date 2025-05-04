from config.config import ConnectDB, load_envs

db_name, username, host, password = load_envs()


class product:
    def __init__(self):
        self.DB = ConnectDB(db_name, username, host, password)
        self.conn, self.curr = self.DB.connect_db()

    def add_product(self, product_id, name, category, price, stock_quantity):
        query = "INSERT INTO Products (product_id, name, category, price, stock_quantity) VALUES (%s, %s, %s, %s, %s)"
        self.curr.execute(query, (product_id, name, category, price, stock_quantity))
        self.conn.commit()

    def get_product(self):
        query = "SELECT * FROM Products"
        self.curr.execute(query)
        results = self.curr.fetchall()
        print("All Products:")
        for i, product in enumerate(results):
            print(
                f"\nProduct No: {i+1}\nProduct ID: {product[0]}\nName: {product[1]}\nPrice: {product[2]}"
            )
