from tkinter import*
root=Tk()
Label(root,text='X direction',fg='red',bg='yellow' ).pack(fill=X)
a=Label(root,text='Y direction',fg='red',bg='yellow')
a.pack(side=RIGHT,fill=Y)#for y axis you have mention the side LEFT/RIGHT Y X should be caps
root.mainloop()
