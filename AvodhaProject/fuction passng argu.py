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


