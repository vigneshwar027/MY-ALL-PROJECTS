def fac(n):
    while n>=1:
        r=n*(n-1)
        n-=1
        print(r)
x=int(input('enter the num: '))
fac(x)