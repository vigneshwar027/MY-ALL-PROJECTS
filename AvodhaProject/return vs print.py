# return vs print statement

''' a return will just hold the value inside the name of the func while print stmt directly prints the value '''

def add(x,y):
    c= x+y
    return c
    
def fun(x,y):
    c= x+y
    print('the result of c is',c)

print('the result of return is:',add(2,3))

fun(21,2)