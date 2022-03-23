"""
continue is used to skip the remainder of the loop 
when a particular condition is met and continue with next iterations

break stops the whole loop including the parent loop

pass means to do nothing
"""

for i in range(1,20):
    if i==5:
        continue
    print(i)        
    
    if i==10:
        print('reached 10 and loop broken')
        break        
    if i==8:
        pass
