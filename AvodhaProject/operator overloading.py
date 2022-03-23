class Mobiles:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

#self and another denotes the objects where the overloaded operators are used
    def __add__(self,other): 
        return self.price + other.offer

    #here the less than operator is doing the funct as printing a stmt which means we can define anything to an operator
    def __lt__(self,other):
        print('hi hello') 
        return (self.price + other.offer)

class offer:
    def __init__(self,cc_offer):
        self.offer = cc_offer 

realme = Mobiles('realme',10000)
nokia = Mobiles('nokia', 5000)
off = offer(200)

# here for defining the function of the + operator codes are written in 6th line
print(realme < nokia) 

#note that the variables of the another class also can be called anywhere in the program using that class's object.
print(realme + off) 

