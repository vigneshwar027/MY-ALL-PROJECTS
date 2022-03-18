def primenum(n):
    for i in range (2,n-1):
       if n%i==0:
            x=0
            break
       else:
        x=1
    return x
a=int(input('enter the number to be checked: '))
if primenum(a)==0:
    print('the num is not prime')
else:
    print('the num is prime')