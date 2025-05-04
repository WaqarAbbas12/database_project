from config.config import ConnectDB, load_envs

db_name, username, host, password = load_envs()


class customer:
    def __init__(self):
        self.DB = ConnectDB(db_name, username, host, password)
        self.conn, self.curr = self.DB.connect_db()

    def add_customer(self, name, phone, email, address):
        qeury = "INSERT INTO Customers (name, phone, email, address) VALUES (%s, %s, %s, %s)"
        self.curr.execute(qeury, (name, phone, email, address))
        self.conn.commit()

    def get_customers(self):
        self.curr.execute("SELECT * FROM Customers")
        results = self.curr.fetchall()
        print("All Customers:")
        for i, customer in enumerate(results):
            print(
                f"\nCustomer No: {i+1}\nCustomer ID: {customer[0]}\nName: {customer[1]}\nPhone: {customer[2]}\nEmail: {customer[3]}"
            )
