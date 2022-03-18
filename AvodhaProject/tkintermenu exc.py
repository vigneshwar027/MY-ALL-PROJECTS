from tkinter import *

def fun():
    print('an option is clicked')

root=Tk()
root.title('Vickys  Notepad')
root.geometry('500x400')
menubar=Menu(root)
root.config(menu=menubar)
fileoption=Menu(menubar,tearoff=0)
editoption=Menu(menubar)
formatoption=Menu(menubar)
viewoption=Menu(menubar)
helpoption=Menu(menubar)

menubar.add_cascade(label='file',menu=fileoption)
fileoption.add_command(label='New',command=fun)
fileoption.add_command(label='New window',command=fun)
fileoption.add_command(label='Open',command=fun)
fileoption.add_command(label='Save',command=fun)
fileoption.add_command(label='Save as',command=fun)

menubar.add_cascade(label='Edit',menu=editoption)
editoption.add_command(label='Cut',command=fun)
editoption.add_command(label='Copy',command=fun)
editoption.add_command(label='paste',command=fun)

menubar.add_cascade(label='Format',menu=formatoption)
formatoption.add_command(label='Wordwrap',command=fun)
formatoption.add_command(label='Font',command=fun)

menubar.add_cascade(label='View',menu=viewoption)
viewoption.add_command(label='zoom',command=fun)
viewoption.add_command(label='statusbar',command=fun)

menubar.add_cascade(label='Help',menu=helpoption)
helpoption.add_command(label='view help',command=fun)


root.mainloop()