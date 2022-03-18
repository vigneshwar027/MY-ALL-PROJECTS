
def bmi(a,b):
    b=b/100 #cm to mtrs
    c=b*b #mtr to sq mtr
    r=(a/c)
    return r

x=int(input('enter your weight: '))
y=int(input('enter your height in cms: '))

print('your BMI is: ',bmi(x,y))
