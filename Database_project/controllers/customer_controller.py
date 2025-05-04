from models.customer import customer


class CustomerController:
    def __init__(self):
        self.model = customer()

    def create_customer(self, name, phone, email, address):
        self.model.add_customer(name, phone, email, address)

    def list_customers(self):
        return self.model.get_customers()
