'''
and returns 1st value if thats is false returns next value
or returns 2nd value if thats is false returns previous value
not returns True or false 
''' 

a,b = False,10

print(a and b)
print(a or b)
print( not a )

# idenity operator

today = 'monday'
yoga_day = 'friday'

if today is yoga_day:
    print('do yoga')
elif today is not yoga_day:
    print('go sleep') 


# membership operator

week = ['monday', 'yoga_day','wednesday']

if 'yoga_day' in week:
    print('attend yoga')
elif 'yoga_day' not in week:
    print('no  yoga day to attend')

