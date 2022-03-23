class SuperMarket:

    '''this is about the supermarket'''
print(SuperMarket.__doc__) #prints the docstring

rice = SuperMarket()
oil = SuperMarket()
shampoo = SuperMarket()

rice.brand = 'samba'
rice.price = 25
rice.stock = 20

oil.brand = 'gold winner'
oil.price = 25
oil.stock = 12

print(rice.__dict__) #prints all elements in the obj




