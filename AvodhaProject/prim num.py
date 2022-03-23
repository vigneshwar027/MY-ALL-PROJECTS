a=int(input('enter the number: '))
num = 'Prime'
for i in range (2,a-1):
    if a%i == 0:
        print(a, ' is not prime')
        num = None
        break
if num == "Prime":
        print(a, ' is prime')

