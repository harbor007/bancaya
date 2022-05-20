CREATE DATABASE bancaya;

USE bancaya;

CREATE TABLE customers (
    customer_id INT,
    customer_firstname CHAR,
    customer_lastname CHAR,
    customer_phonenumber INT,
    customer_curp CHAR,
    customer_rfc CHAR,
    customer_address CHAR,
    PRIMARY KEY(customer_id)
);

CREATE TABLE items (
    item_id INT,
    item_name CHAR,
    item_price FLOAT,
    PRIMARY KEY(item_id)
);

CREATE TABLE sold_items (
    order_id INT NOT NULL,
    customer_id INT NOT NULL,
    item_id INT NOT NULL,
    order_date DATE,
    order_price FLOAT,
    order_comments CHAR,
    PRIMARY KEY(order_id),
    FOREIGN KEY(customer_id)
		REFERENCES customers(customer_id),
	FOREIGN KEY(item_id)
		REFERENCES items(item_id)
);