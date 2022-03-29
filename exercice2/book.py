import pandas

# Defining the Order class, that handles the different orders we have

class Order:

    # Both SELL and BUY are treated as elements of type Order. They have a type, quantity, price and identifier
    def __init__(self, typeTransac, quantity, price, ide):
        
        if (typeTransac == "BUY" or typeTransac == "SELL"):   

            self.typeTransac = typeTransac
            self.id = ide
            self.price = price
            self.quantity = quantity
        else:

            print("Error : unrecognizeg transaction type ...")

    
    # Overriding the str function so that we can easily print orders whenever we want

    def __str__(self):
        return str(self.typeTransac) + " " + str(self.quantity) + "@" + str(self.price) + " id=" + str(self.id)



# Defining the Book class

class Book:


    # A book is defined by its name. At the creation, we give the id of the very first transaction (id=1) and an empty history of transactions
    def __init__(self, name="book"):

        self.id = 1
        self.history = []

        if(type(name) == str):

            self.name = name

        else:
            self.name = "book"


    # This function is called to add a purchase
    def insert_buy(self, quantity, unitaryPrice):
        
        # We create an Order with the given attributes
        newBuy = Order("BUY", quantity, unitaryPrice, self.id)
        self.id += 1

        # We add the new Order to the history
        self.history.append(newBuy)
        
        # We print what happened to let the user know the current state of the history
        print("--- Insert ", end = "")
        print(newBuy, end = "")
        print(" on ", self.name, end = "\n")
        
        # We sort the history according to the price before displaying it
        self.order()
        print(self)


    # This function is called to add a sale    
    def insert_sell(self, quantity, unitaryPrice):

        # We create an Order with the given attributes
        newSell = Order("SELL", quantity, unitaryPrice, self.id)
        self.id += 1

        # We print what happened to let the user know the current type of the history
        print("--- Insert ", end = "")
        print(newSell, end = "")
        print(" on", self.name, end = "\n")

        # We check if any execution(s) should be made
        self.execute(newSell)
        
        # We sort the history according to the price before displaying it
        self.order()
        print(self)

    
    # This functions sorts the history according to the price
    def order(self):

        self.history = sorted(self.history, key = lambda order : order.price, reverse = True)
        

    # This function is called during sales.
    def execute(self, order):

        # buyList contains the list of bought items. totalQuantitiesBuy is the sum of the quantities of buyList
        buyList = [buy for buy in self.history if buy.typeTransac == "BUY"]
        totalQuantitiesBuy = sum(buy.quantity for buy in buyList)
    
        # We initialize an index that will go over buyList
        index = 0
        quantity = order.quantity

        # if quantity is lower than totalQuantitiesBuy, we must make an execute
        if quantity < totalQuantitiesBuy:
            
            # while we still have quantities to remove
            while quantity > 0 and index < len(buyList):

                print("Execute", end = " ")

                
                tempList = [i for i in self.history if i.id == buyList[index].id]
                
                # element is the indexth item of buyList. ind is its index in the self.history.
                element = tempList[0]
                ind = self.history.index(element)

                # if we can remove it all:
                if quantity < buyList[index].quantity:

                    self.history[ind].quantity -= quantity
                    quantity = 0

                    print(order.quantity - quantity, "at", element.price, end = " ")

                # else, it means we must remove element from self.history and re-loop because we still have some items in excess in the SELL
                else:
                    x = element
                    self.history.remove(element)
                    quantity -= x.quantity

                    print(x.quantity, "at", x.price, end = " ")
                    
                index += 1

                print("on", self.name)
            


        # else, we simply add the order to the history
        else:

            self.history.append(order)

    #fonction exo5
    def visualisationPandas(self):

        #creation of a dataframe for the SELL orders
        dfSell = pandas.DataFrame({'Quantity': pandas.Series([sells.quantity for sells in self.history if sells.typeTransac == "SELL"], index = [sells.id for sells in self.history if sells.typeTransac == "SELL"]), 'Price': pandas.Series([sells.price for sells in self.history if sells.typeTransac == "SELL"], index = [sells.id for sells in self.history if sells.typeTransac == "SELL"])})
        print("\nSELL Orders:")
        print(dfSell)
        
        #creation of a dtaframe for the BUY orders
        dfBuy = pandas.DataFrame({'Quantity': pandas.Series([buy.quantity for buy in self.history if buy.typeTransac == "BUY"], [buy.id for buy in self.history if buy.typeTransac == "BUY"]), 'Price': pandas.Series([buy.price for buy in self.history if buy.typeTransac == "BUY"], index = [buy.id for buy in self.history if buy.typeTransac == "BUY"])})
        print("\nBUY Orders:")
        print(dfBuy)

        #creation of a dataframe with all the orders sorted by id
        dfBook = pandas.DataFrame({'Type': pandas.Series([sells.typeTransac for sells in sorted(self.history, key=lambda x : x.id)], index = [sells.id for sells in sorted(self.history, key=lambda x : x.id)]), 'Quantity': pandas.Series([sells.quantity for sells in sorted(self.history, key=lambda x : x.id)], index = [sells.id for sells in sorted(self.history, key=lambda x : x.id)]), 'Price': pandas.Series([sells.price for sells in sorted(self.history, key=lambda x : x.id)], index = [sells.id for sells in sorted(self.history, key=lambda x : x.id)])})
        print("\nAll Orders:")
        print(dfBook)


    # Overriding the str function so that we can easily print orders whenever we want
    def __str__(self):

        s = "Book on " + self.name + "\n"

        for transaction in self.history:
            s += "\t" + str(transaction) + "\n"
            
        s += "------------------------"

        return s





























