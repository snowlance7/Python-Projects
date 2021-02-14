import sqlite3
import business as b
db_path = "guitar_shop.sqlite"

with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.executescript("guitar_shop.sql")
        conn.commit()
        c.close

def getCategory(category):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        result = c.execute("SELECT * FROM Category WHERE categoryName = '" + category.categoryName +"'")
        category.categoryID = result[0]

def getProducts(category):
    products = []

    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        for product in c.execute("SELECT productCode,productName,listPrice FROM Product WHERE categoryID = '" + str(category.categoryID) + "'"):
            products.append(b.Product(product[0],product[1],product[2]))
        return products

def getProduct(code):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        product = c.execute("SELECT productName,listPrice FROM Product WHERE productCode = '" + str(code) + "'")
        return b.Product(code,product[0],product[1])

def updateProduct(product):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        conn.commit()
    c.execute("UPDATE Product SET listPrice = " + str(product.listPrice) + " WHERE productCode = '" + str(product.productCode) + "'")

with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        for row in c.execute("SELECT categoryName FROM Category"):
            print(row[0])