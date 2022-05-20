from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

db = client.test

customers = db.customers
items = db.items
sales = db.items

data = {"customers_data": [
    {"firstname":"Bruce","lastname":"Wayne"},
    {"firstname":"Clark","lastname":"Kent"},
    {"firstname":"Tony","lastname":"Stark"}
  ],
  "items_data": [
    {"title":"USM","price":10.2},
    {"title":"Mouse","price":12.23},
    {"title":"Monitor","price":199.99}
  ]
}

data_sales = {
    "sales": [
    {"customer_id":1,"item_purchased":1,"date":"2022-05-20"},
    {"customer_id":2,"item_purchased":5,"date":"2022-05-22"},
    {"customer_id":3,"item_purchased":6,"date":"2022-05-21"}
    ]
}

for customer_ in data['customers_data']:
    customers.insert_one(customer)

for items_ in data['items_data']:
    items.insert_one(items_)

for sales_ in data_sales['items_data']:
    sales.insert_one(sales_)