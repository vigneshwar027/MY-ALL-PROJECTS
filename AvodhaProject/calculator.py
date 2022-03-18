    import parser
from tkinter import *
root=Tk()
heading=Label(root,text='VICKYS CALCULATOR',fg='red',bg='yellow',font='times')
heading.grid(row=0,columnspan=6)
disp=Entry(root)
disp.grid(row=1,columnspan=6)
i=0
def getdata(num):
    global i
    disp.insert(i,num)
    i+=1
def clearall():
    disp.delete(0,END)

def undo():
    es=disp.get()
    bs=es[:-1]
    clearall()
    disp.insert(0,bs)

def calculate():
    try:
        a=disp.get()
        a=parser.expr(a).compile()
        result=eval(a)
        clearall()
        disp.insert(0,result)
    except:
        disp.insert(0,error)
Button(root,text='7',command=lambda :getdata(7)).grid(row=5,column=0)
Button(root,text='8',command=lambda :getdata(8)).grid(row=5,column=1)
Button(root,text='9',command=lambda :getdata(9)).grid(row=5,column=2)
Button(root,text='4',command=lambda :getdata(4)).grid(row=6,column=0)
Button(root,text='5',command=lambda :getdata(5)).grid(row=6,column=1)
Button(root,text='6',command=lambda :getdata(6)).grid(row=6,column=2)
Button(root,text='1',command=lambda :getdata(1)).grid(row=7,column=0)
Button(root,text='2',command=lambda :getdata(2)).grid(row=7,column=1)
Button(root,text='3',command=lambda :getdata(3)).grid(row=7,column=2)
Button(root,text='0',command=lambda :getdata(0)).grid(row=8,column=0)

Button(root,text='.',command=lambda :getdata('.')).grid(row=8,column=1)
Button(root,text='%',command=lambda :getdata('%')).grid(row=4,column=3)
Button(root,text='/',command=lambda :getdata('/')).grid(row=5,column=3)
Button(root,text='*',command=lambda :getdata('*')).grid(row=6,column=3)
Button(root,text='-',command=lambda :getdata('-')).grid(row=7,column=3)
Button(root,text='+',command=lambda :getdata('+')).grid(row=4,column=2)
Button(root,text='(',command=lambda :getdata('(')).grid(row=4,column=0)
Button(root,text=')',command=lambda :getdata(')')).grid(row=4,column=1)
Button(root,text='=',command=lambda :calculate()).grid(row=8,column=3)
Button(root,text='<-',command=lambda :undo()).grid(row=8,column=2)
Button(root,text='AC',command=lambda :clearall()).grid(row=4,column=4)
Button(root,text='00',command=lambda :getdata('00')).grid(row=5,column=4)
Button(root,text='PI',command=lambda :getdata(3.14)).grid(row=6,column=4)
Button(root,text='^',command=lambda :getdata('**')).grid(row=7,column=4)
root.mainloop()
