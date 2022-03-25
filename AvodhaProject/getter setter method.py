class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def change_name(self):
        self.name = 'parrot'

    def get_name(self):
        print(self.name)

cat = Animal('cat')
#pls dont forget to use brackets while calling a function unlike variable
cat.change_name() 
cat.get_name()


def add(x,y):
    c= x+y
    return c

print(add(2,3))

