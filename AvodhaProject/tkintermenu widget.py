# # step1: assign a name for your menu bar under Menu(root)
# # step2: config menu to the assigned name (root.config menu='assigned name')
# #
# # step3: create fileoptions for the assigned menubar so that you can create sub menus to it.

from  tkinter import *
root=Tk()
mymenubar=Menu(root) #step1
root.config(menu=mymenubar) #step2
def new():
    print('new option clicked')

filemenu=Menu(mymenubar) #step3
editmenu=Menu(mymenubar) #step3

mymenubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='new',command=new) 

mymenubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='cut',command=new)
root.mainloop()

