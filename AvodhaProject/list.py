list1=['z','e','set','z']
list2=['sa','re','ga','ma']
print(list(enumerate(list1))) #u have to wrap in inside a list
print(sorted(list1))    #sorts the list
print(list1[::-1]) #diaplays the elememt in reverse

list1.append('lusu') #add at atlast
list1.remove('e') #remove the element
list1.extend([27,'wew',12]) #appending multiple items at end of list
list1.insert(2,'enna valka ithu') #add at specific index
print(list1+list2)
list1[3]='vena philips su' #updation
print(list1[2:4]) #slicing
list2[-1]='poda angutu' #updation in reverse

print(list1)
print('sa' in list2) #checks availability and returns true or false
len(list1) #checks length
del(list1[1]) #delete item


# print list elements inside a list
'''
to access the elements of list or tuple 
call the identifier and mention the respective index value as required
like in below exmaple
'''

a= [1,2,(23,43,'hi'),'he',['love',12,'no']]

print(a[4][0],a[2][2]) # this print love and hi