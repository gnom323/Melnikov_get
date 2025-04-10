from tkinter import *

def calculate(*args):
    try:
        value_1 = float(num_1.get()) 
        value_2 = float(num_2.get()) 
        value_3 = float(num_3.get()) 

        value_4 = float(num_4.get()) 
        value_5 = float(num_5.get()) 
        value_6 = float(num_6.get()) 

        value_7 = float(num_7.get()) 
        value_8 = float(num_8.get()) 
        value_9 = float(num_9.get()) 

        determinant.set(value_1*(value_5*value_9-value_6*value_8)-value_2*(value_4*value_9-value_7*value_6)+value_3*(value_4*value_8-value_5*value_7))
    except ValueError:
        pass

def delete(*args):
    num_1.set('')
    num_2.set('') 
    num_3.set('') 
    num_4.set('') 
    num_5.set('') 
    num_6.set('')
    num_7.set('') 
    num_8.set('') 
    num_9.set('')
    determinant.set('')
        
root = Tk()
root.title("Детерминант")

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
num_1 = StringVar()
entry_num_1 = Entry(mainframe, width=15, textvariable=num_1)
num_2 = StringVar()
entry_num_2 = Entry(mainframe, width=15, textvariable=num_2)
num_3 = StringVar()
entry_num_3 = Entry(mainframe, width=15, textvariable=num_3)

num_4 = StringVar()
entry_num_4 = Entry(mainframe, width=15, textvariable=num_4)
num_5 = StringVar()
entry_num_5 = Entry(mainframe, width=15, textvariable=num_5)
num_6 = StringVar()
entry_num_6 = Entry(mainframe, width=15, textvariable=num_6)

num_7 = StringVar()
entry_num_7 = Entry(mainframe, width=15, textvariable=num_7)
num_8 = StringVar()
entry_num_8 = Entry(mainframe, width=15, textvariable=num_8)
num_9 = StringVar()
entry_num_9 = Entry(mainframe, width=15, textvariable=num_9)

entry_num_1.grid(column=1, row=1)
entry_num_2.grid(column=2, row=1)
entry_num_3.grid(column=3, row=1)

entry_num_4.grid(column=1, row=2)
entry_num_5.grid(column=2, row=2)
entry_num_6.grid(column=3, row=2)

entry_num_7.grid(column=1, row=3)
entry_num_8.grid(column=2, row=3)
entry_num_9.grid(column=3, row=3)

entry_num_1.focus()
determinant = StringVar()

Label(mainframe, textvariable=determinant).grid(column=2, row=4, sticky=(W, E))
Button(mainframe, text="Детерминант", command=calculate, height=3).grid(column=1, row=4, sticky=E)
Button(mainframe, text="Очистить", command=delete, height=3).grid(column=1, row=5)

root.mainloop()