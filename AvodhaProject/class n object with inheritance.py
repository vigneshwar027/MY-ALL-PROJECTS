class computer:
    
    '''this class is avout the laptop specs'''
    # print(computer.__doc__)
    # help(computer)# no indent needed for ths 2 lines

    def __init__(self,):
        self.brand = 'ACer'

    def getspecs(self):
        self.specs=(input('the specs of the computer: '))

    def displayspecs(self):
        print('the specs of the computer is: ',self.specs)

class desktop(computer):
        def w(self):
            weight = (input('the weight of the desktop: '))
            print('the weight of the desktop is: ',weight)
            


class laptop(computer):
    def c(self):
        color = (input('the color of the laptop: '))
        print('the color of the laptop ',color)

c1=computer()
d1=desktop()
l1=laptop()
d1.getspecs()
d1.displayspecs()
d1.w()
l1.getspecs()
l1.displayspecs()
l1.c()



class student:
    def __init__(self, name,age):
        self.name=name
        self.age=age
        print('\n',self.name)
        print(self.age)
o1=student('vijay',21)
o2=student('arun',25)


print(d1.brand)
d1.getspecs
