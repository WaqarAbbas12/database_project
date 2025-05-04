from config.config import ConnectDB, load_envs
from controllers.invoice_controller import InvoiceController
from controllers.product_controller import ProductController
from controllers.customer_controller import CustomerController
from controllers.purchase_controller import PurchaseController
from controllers.supplier_controller import SupplierController
from controllers.invoice_detail_controller import InvoiceDetailController
from views.views import Views
import atexit

db_name, username, host, password = load_envs()
DB = ConnectDB(db_name, username, host, password)
conn, curr = DB.connect_db()
atexit.register(conn.close)


def main(conn, curr):
    flag = True
    invoice_detail_controller = InvoiceDetailController()
    invoice_controller = InvoiceController()
    customer_controller = CustomerController()
    product_controller = ProductController()
    purchase_controller = PurchaseController()
    supplier_controller = SupplierController()
    views = Views()

    while flag:
        print(
            "==========Inventory and Billing System==========\n********System Menu********"
        )
        print(
            "1:View all Invoices\n2:View specific Invoice\n3:View Customer details\n4:Get Products\n5:View Purchases\n6:Get all Suppliers"
        )
        print("0:Exit")

        choice = input("Choice:")

        if choice == "1":
            invoice_detail_controller.list_invoice_details()

        elif choice == "2":
            id = int(input("Invoice ID:"))
            invoice_controller.list_invoice(id)

        elif choice == "3":
            customer_controller.list_customers()

        elif choice == "4":
            product_controller.list_products()

        elif choice == "5":
            purchase_controller.list_purchases()

        elif choice == "6":
            supplier_controller.list_suppliers()

        elif choice == "0":
            flag = False
            break
        else:
            continue


if __name__ == "__main__":
    main(conn, curr)
