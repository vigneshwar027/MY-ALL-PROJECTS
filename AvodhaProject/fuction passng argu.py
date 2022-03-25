def fac(n):
    while n>=1:
        r=n*(n-1)
        n-=1
        print(r)
x=int(input('enter the num: '))
fac(x)

# passing str in arguments
def name(name):
    print('the name is',name)

name('vuck')

#default argument that if incase no arg is passed in func call then the def value in the fun def will be used 
def info(name='Unknown'): 
    print('the name is',name)

info()

#key word arguments
def keyarg(a,b,d,c=10):
    res = a**b+c+d
    print(res)

keyarg(d=4,b=2,a=2)#in this way u can pass values in any sequence


#variable len arguments
#when uu r not sure how many args will be passed
def keyarg(*users):
    
    print('the following are the users:',users)

keyarg('vijay','vikram','vicky')


############################


# def det(name,age, sex):
#     print(name)

# det('vick', 21, sex = 'male' ) #u can use positional arg along with key word but pos.arg should given 1st

def total(name,age, *marks): #variable length arguments
    summ = 0
    for i in marks:
        summ = summ + i
    print(name, age, 'Total=',summ)

total('vick', 21, 78,76,76,76,76) 
#u can use positional arg along with key word but pos.arg should given 1st


#variable lenghth keyword arguments

def data(**scores): # variable length keyword arguments
    for name,mark in scores.items(): #while accessing dictionaries in loops u shd specify if u need items or keys or values. 
        print(name,': Scored',mark)
        



data(mano=27,vick=32,rocky=43)

a= {'mano': 27, 'vick': 32, 'rocky': 43}

for i in a():
    print(i)