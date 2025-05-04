-- Create a database
CREATE DATABASE inventory_billiing_system;
USE inventory_billiing_system;

-- Define Tables
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(255)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT
);

CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    contact VARCHAR(20),
    address VARCHAR(255)
);

CREATE TABLE Purchases (
    purchase_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    supplier_id INT,
    quantity INT,
    purchase_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Invoices (
    invoice_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    invoice_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Invoice_Details (
    invoice_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    invoice_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (invoice_id) REFERENCES Invoices(invoice_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Insert Dummy data
INSERT INTO Customers (name, phone, email, address) VALUES
('John Doe', '1234567890', 'john@example.com', '123 Elm Street'),
('Jane Smith', '9876543210', 'jane@example.com', '456 Oak Avenue'),
('Mike Johnson', '5556667777', 'mike@example.com', '789 Pine Road');

INSERT INTO Products (name, category, price, stock_quantity) VALUES
('Laptop', 'Electronics', 800.00, 50),
('Smartphone', 'Electronics', 500.00, 100),
('Desk Chair', 'Furniture', 120.00, 30),
('Notebook', 'Stationery', 5.50, 200);

INSERT INTO Suppliers (name, contact, address) VALUES
('Tech Distributors', '1122334455', '321 Tech Street'),
('Office Supplies Co.', '9988776655', '654 Stationary Lane'),
('Furniture Depot', '7766554433', '987 Furniture Plaza');

INSERT INTO Purchases (product_id, supplier_id, quantity, purchase_date) VALUES
(1, 1, 20, '2025-04-01'),
(2, 1, 50, '2025-04-02'),
(3, 3, 10, '2025-04-03'),
(4, 2, 100, '2025-04-04');

INSERT INTO Invoices (customer_id, invoice_date) VALUES
(1, '2025-04-05'),
(2, '2025-04-06'),
(3, '2025-04-07');

INSERT INTO Invoice_Details (invoice_id, product_id, quantity, price) VALUES
(1, 1, 1, 800.00),
(1, 4, 5, 5.50),
(2, 2, 2, 500.00),
(3, 3, 1, 120.00);


-- Define Views
CREATE VIEW invoice_summary_view AS
SELECT c.name AS customer_name, i.invoice_id, i.invoice_date, p.name AS product_name, id.quantity, id.price
FROM Invoices i
JOIN Customers c ON i.customer_id = c.customer_id
JOIN Invoice_Details id ON i.invoice_id = id.invoice_id
JOIN Products p ON id.product_id = p.product_id;

CREATE VIEW low_stock_view AS
SELECT * FROM Products WHERE stock_quantity < 10;


-- Stored Procedures
DELIMITER $$

CREATE PROCEDURE create_invoice(IN cust_id INT, IN prod_ids TEXT, IN quantities TEXT)
BEGIN
    DECLARE new_invoice_id INT;
    INSERT INTO Invoices (customer_id, invoice_date) VALUES (cust_id, CURDATE());
    SET new_invoice_id = LAST_INSERT_ID();

    SET @i = 1;
    WHILE @i <= JSON_LENGTH(prod_ids) DO
        INSERT INTO Invoice_Details (invoice_id, product_id, quantity, price)
        VALUES (
            new_invoice_id,
            JSON_EXTRACT(prod_ids, CONCAT('$[', @i-1, ']')),
            JSON_EXTRACT(quantities, CONCAT('$[', @i-1, ']')),
            (SELECT price FROM Products WHERE product_id = JSON_EXTRACT(prod_ids, CONCAT('$[', @i-1, ']')))
        );
        SET @i = @i + 1;
    END WHILE;
END$$

CREATE PROCEDURE update_stock(IN prod_id INT, IN qty INT)
BEGIN
    UPDATE Products SET stock_quantity = stock_quantity - qty WHERE product_id = prod_id;
END$$

DELIMITER ;

-- Triggers
DELIMITER $$

CREATE TRIGGER reduce_stock_after_invoice
AFTER INSERT ON Invoice_Details
FOR EACH ROW
BEGIN
    UPDATE Products
    SET stock_quantity = stock_quantity - NEW.quantity
    WHERE product_id = NEW.product_id;
END$$

CREATE TRIGGER increase_stock_after_purchase
AFTER INSERT ON Purchases
FOR EACH ROW
BEGIN
    UPDATE Products
    SET stock_quantity = stock_quantity + NEW.quantity
    WHERE product_id = NEW.product_id;
END$$

DELIMITER ;

-- Functions
DELIMITER $$

CREATE FUNCTION get_total_invoice(inv_id INT) RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE total DECIMAL(10,2);
    SELECT SUM(price * quantity) INTO total FROM Invoice_Details WHERE invoice_id = inv_id;
    RETURN total;
END$$

CREATE FUNCTION get_stock(prod_id INT) RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE qty INT;
    SELECT stock_quantity INTO qty FROM Products WHERE product_id = prod_id;
    RETURN qty;
END$$

DELIMITER ;

