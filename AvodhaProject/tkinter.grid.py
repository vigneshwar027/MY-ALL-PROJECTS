from tkinter import *
root=Tk()

Label(root,text='Enter the below credentials').grid(row=0,column=0)
root.title('My site')
root.geometry('500x200')
Label(root,text='Username:').grid(row=1,column=0)
Label(root,text='Password:').grid(row=2,column=0)
Entry(root).grid(row=1,column=1)
Entry(root).grid(row=2,column=1)
root.mainloop()

