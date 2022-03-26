class Order:

    def __init__(self, typeTransac, quantity, price, ide):
        
        if (typeTransac == "BUY" or typeTransac == "SELL"):   

            self.typeTransac = typeTransac
            self.id = ide
            self.price = price
            self.quantity = quantity
        else:

            print("Error : unrecognizeg transaction type ...")


    def __str__(self):
        return str(self.typeTransac) + " " + str(self.quantity) + "@" + str(self.price) + " id=" + str(self.id)




class Book:

    def __init__(self, name="book"):

        self.id = 1
        self.history = []

        if(type(name) == str):

            self.name = name

        else:
            self.name = "book"


    def insert_buy(self, quantity, unitaryPrice):
        
        newBuy = Order("BUY", quantity, unitaryPrice, self.id)
        self.id += 1

        self.history.append(newBuy)
        

        print("--- Insert ", end = "")
        print(newBuy, end = "")
        print(" on ", self.name, end = "\n")
        
        self.order()
        print(self)


        
    def insert_sell(self, quantity, unitaryPrice):

        newSell = Order("SELL", quantity, unitaryPrice, self.id)
        self.id += 1
        
        self.history.append(newSell)

        print("--- Insert ", end = "")
        print(newSell, end = "")
        print(" on ", self.name, end = "\n")

        self.order()
        print(self)


    def order(self):

        temp = sorted(self.history, key = lambda order : order.price, reverse = True)
        self.history = sorted(temp, key = lambda order : order.typeTransac, reverse = True)


    def __str__(self):

        s = "BOOK ON " + self.name + "\n"

        for transaction in self.history:
            s += "\t" + str(transaction) + "\n"
            
        s += "-----------------------------"

        return s

















