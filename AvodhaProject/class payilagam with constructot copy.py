import sys

class SuperMarket:
    # class variables available throughout the class and can be called using the class ot any object name
    name = 'VIGNESHWAR SUPERMARKET'
    place = 'Trichy'


    #the below is the constructor that constructs the object specific variables
    def __init__(self,brand,price,stock):
        self.brand = brand
        self.price = price
        self.stock = stock

    #the instance/object method is something that uses the instance/object variables and you call a object/instance method using a object
    def place(self):
        print('in this instance method', self.brand)

    
    #the class method is something that uses the class variables and you call a object method using the class or its objects
    @classmethod
    def info(cls):
        print('the name of the market is', cls.name)

    @staticmethod
    def staticmethod(num1, num2):
        result = num1+num2
        print('the result is printed by calling static method',result)
    
rice = SuperMarket('samba',12.32,12)
oil = SuperMarket('gold winner',12.32,12)
cake = SuperMarket('black forest',200.2,14)

print(rice.__dict__) #prints all elements in the obj
print(oil.price)
print(cake.brand)
print(SuperMarket.name)

#calling the class method
SuperMarket.info()
oil.info()

#calling the instance/object method
oil.place()

#calling the instance/object method
SuperMarket.staticmethod(2,3)
oil.staticmethod(2,3)

#a class object can be accessed by the objects also like this but still it is practised rarely and not a good practice
print(oil.name) 

#the class object can be modified to any specific objects like this
cake.name = 'divya shop'
print(cake.name) 

''' self variables means object specific variables 
whereas static variables means class variables'''

# go through the below class and see the putput to understand how all the variable gets changed
class Test:
    a=100
    def __init__(self):
        self.b = '100'

    def ppl(self,name):
        print('the name is ',name)
        
t=Test()
print(t.b)
print(t.a)
t.a = 777
print(t.a)
print(Test.a)
anu = Test()
anu.ppl('sowmni')

ans = input('Do you want to exit? (y/n): ')
if ans == 'y':
    sys.exit() #exits the running program
else :
    pass
