from config.config import ConnectDB, load_envs

db_name, username, host, password = load_envs()


class supplier:
    def __init__(self):
        self.DB = ConnectDB(db_name, username, host, password)
        self.conn, self.curr = self.DB.connect_db()

    def add_supplier(self, supplier_id, name, contact, address):
        query = "INSERT INTO Suppliers (supplier_id, name, contact, address) VALUES (%s, %s, %s, %s)"
        self.curr.execute(query, (supplier_id, name, contact, address))
        self.conn.commit()

    def get_supplier(self):
        query = "SELECT * FROM Suppliers"
        self.curr.execute(query)
        results = self.curr.fetchall()
        print("All Suppliers:")
        for i, supplier in enumerate(results):
            print(
                f"\nSupplier No: {i+1}\nSupplier ID: {supplier[0]}\nName: {supplier[1]}\nContact: {supplier[2]}"
            )
