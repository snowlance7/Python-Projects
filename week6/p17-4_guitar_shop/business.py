import database as db

class Category():
    def __init__(self,categoryName):
        self.categoryID = int()
        self.categoryName = categoryName

    def getProducts(self):
        db.getCategory(self)
        return db.getProducts(self)

class Product(Category):
    def __init__(self,productCode,productName,listPrice):
        self.productCode = productCode
        self.productName = productName
        self.listPrice = listPrice
    
    def UpdateProduct(self):
        db.updateProduct(self)        

        