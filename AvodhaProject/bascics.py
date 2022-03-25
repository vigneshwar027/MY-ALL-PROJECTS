def address(a,b,c):
    return a+b, b+c, c+a #note a fun can return mulitple results 


a= 12
# print(id(a)) #gives the memory address

result = address(21,21,2)
print(address(21,2,3))

print(len(result))

for i in (result): # i by default rep tha elements of the list/tuple and there is no need to refer the index or len of the resp elements.
    print(i)