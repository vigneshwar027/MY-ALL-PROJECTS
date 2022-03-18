try:

    dic1={'egg':5,'onion':50,'carrot':20,'brinjal':15}
    print('list of available items')
    for x in dic1:
        print(x)
    print()
    a=input('enter the product to know the price: ')

    print('{}{}'.format(dic1[a],'rupees'))
except:
    print('entry out of the list/invalid')