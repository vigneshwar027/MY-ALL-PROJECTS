a=int(input('enter the number: '))
for i in range (2,a-1):
    if a%i==0:
        print(a, ' is not prime')
        break
    else:
        print(a, ' is prime')
        break
