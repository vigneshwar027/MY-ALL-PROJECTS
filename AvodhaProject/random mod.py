from random import * 
# import random if u import like this u need to class its func using the module name
#eg: random.choices 

for i in range (20):
    print(randint(100,200))


list = [1,3,4]

# for i in range(50):

#     c= int(str(random.choice(list)) + str(random.choice(list)))

#     if c%2 != 0:
#         print(c)

print(choice(list))