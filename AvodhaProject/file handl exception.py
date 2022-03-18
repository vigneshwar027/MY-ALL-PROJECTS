a=open('demo.txt','w')
b=a.write('hi avodha')
a=open('demo.txt','r')
c=a.read()
print(c)
a=open('demo.txt','a+')
d=a.write(' how are you')
a=open('demo.txt','r')
e=a.read()


