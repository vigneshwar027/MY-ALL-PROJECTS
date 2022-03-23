x= lambda a,b,c,d: ((a*6)+c)/d # used to create a function in a single statement # no need of colon
print(x(12,56,2,4))


# lambda using map function
items = [2,3,30,17,20,3]
y=list(map(lambda x,y: x*y ,items,items)) #here you directly pass multiple argument
print(y)

# lambda using filter function

z=list(filter(lambda x: x>3 ,items))
print(z)

