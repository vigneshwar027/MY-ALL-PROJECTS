from tkinter import*
root=Tk() #step 1 declare a variable to tkinter class
f1=Frame(root).pack() #Frame is a class and it should be declared to a variable
#f1
Label(root,text='hello vicky',fg='red',bg='yellow').pack() #Label not label
Label(root,text='all best for your works',bg='red',fg='yellow').pack()
root.title('My Website')
root.geometry('720x720')
def login():
    print('you have successfully logged in')
def logout():
    print('you have successfully logged out')
Button(f1,text='Log in Here',bg='blue',fg='red',command=login).pack()
Button(f1,text='log out',bg='yellow',fg='red',command=logout).pack()
#note: no '' used b/w keywords eg like:'text'
root.mainloop() #last step closing the function