# global local variables
name = 'Aathvika'

def changed_name():
    
  name = 'Pranu'
  print('The changed name is:', name,'\n but the previous name was', globals()['name'])
  #globals to call the global variable, remember the above syntax for globals
    
def change_global_name():
    global name
    name = 'Pranu'

changed_name()
change_global_name()

print(' the changed global name is:', name)
#global to call the global variable tp change/update it inside the function
