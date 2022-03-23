class HeadOffice:
    place = 'Chennai'

    def __init__(self) -> None:
        self.ho_offer = 1000

class Branch(HeadOffice):
    place = 'Trichy'
    def __init__(self) -> None:
        
        #to access the init varibles of the super class 
        super().__init__()

        self.bo_offer = 500

branch_cus1 = Branch()
print(branch_cus1.ho_offer)


#accessing the parent class's objectspecific variables with arguments

class Human:
    def __init__(self,name,gender,age) -> None:
        self.name = name
        self.gender = gender
        self.age = age


class Employee(Human):
    def __init__(self,name,id,salary) -> None:
        super().__init__(name,'female',20)
        self.name = name
        self.id = id
        self.salary = salary

emp1 = Employee('rita','007',25000)

print(emp1.name)
print(emp1.age)
print(emp1.gender)
