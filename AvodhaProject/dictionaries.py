'''
a dicitionary key should always be string
but the value can be anything
'''

try:

    dic1={'egg':5,'onion':50,'carrot':20,'brinjal':15, 'small dict': {'name':'kumar','age':21}}
    print('list of available items')
    for x in sorted(dic1):
        print(x)
    
    a=input('enter the product to know the price: ')

    print('{}{}'.format(dic1['small dict'],'rupees'))
except:
    print('entry out of the list/invalid')

print('the price of egg is: ',dic1['egg']) #calling elements of dict

if dic1.get("egg"):
    print('the price is' , dic1['egg'])
else:
    print('egg not found')


print(dic1.keys())
print(dic1.items())
print(dic1.values())
# dic1.clear will clear the ele in dic


dic2 = {'name':['kumar','naveen','janu'],'age':(12,13,12)}
# a dic can have many vlaue like in dic
print(dic2['age'][1])


