a=input('enter your caste: ')
b=100
if a=='sc':
    print('the allowed quota is:',b*50/100)
elif a=='bc':
    print('the allowed quota is:',b*30/100)
elif a=='gen':
    print('the allowed quota is:',b*10/100)
else:
    print('no quota')

