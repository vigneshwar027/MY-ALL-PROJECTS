#Encapsulation examples:

''' (Public Variable) and can be accessed anyhwhere in program

    (Protected Variable) and can be accessed only within their class and it's  
    child classes in program however this is not strictly not followed but just a convention see that _b is callable in Class B below

    #(Private Variable) and can be accessed only by its own class and no where else '''

# the same rule applyies to the methods too
#Note that whenever a class or object variables are called outside it's class it has to be called by refering to it's class or object name

# note u can call a class variable with it's object reference
#but can't call a object variable with the class reference.

class A:

    a='Public Variable'
    _b='Protected variable'
    __c='Private variable'

    def __init__(self):
        pass
        
t=A()

class B:
   
    def act(self):
        print(A.a)
        print(A._b)
        # print(A.__c) cant call private variable so using below option to do same
        
        #you can call a private variable only thorough its object and class refernce.
        print(t._A__c) #just add _classname before the private variable

z=B()
z.act()
