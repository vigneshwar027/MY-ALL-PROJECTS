#example for constructor overridiing
class data:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    
    def __init__(self,name,age,sex):
        self.name = name
        self.age  = age
        self.sex  = sex
        
    def study(self):
        print(self.name,self.age,self.sex)


vicky = data('vicky',21,'male')
print ('result of constructor overloading')
vicky.study()





#example for method overridiing
class Mummy:

    def study(self):
        print('medicine or engineering')

class son(Mummy):
    def study(self):
        super().study() #if required to see the func in the super class
        print('my study is coding')

vicky = son()

# in this calling study in child class has overridded the study in parent class
print ('result of method overridding')
vicky.study() 

###############################################

#method overloading where you pass multiple arguments in one method
class Student:

    def mark(self, *contents):        
        list = []
        for i in contents:
            list.append(i) #dont do any assignment for append op. itsjust list.append(i)
        print ('the marks are',list)

vijay = Student()
print ('result of method overloading')
vijay.mark(98,76,65,56,56,65,34)

