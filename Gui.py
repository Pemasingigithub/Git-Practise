from tkinter import *
w=Tk()

w.geometry("520x520")
w.title("Student Management System")
w.config(background='lightgray')

def submit():
    username=entry.get()
    print(username)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)
labal=Label(w,
            text="Enter the password:")
labal.pack(side=LEFT)
entry=Entry(w,
            font='Arial',
            show='*',
            foreground='green',
           )
entry.pack(side=LEFT)

submit_button=Button(w,
                     text='Submit',
                     command=submit,
                    )
submit_button.pack(side=RIGHT)

delete_button=Button(w,
                     text='Delete',
                     command=delete,
                    )
delete_button.pack(side=RIGHT)

backslace_button=Button(w,
                        text='Backspace',
                        command=backspace,

                        )
backslace_button.pack(side=RIGHT)

def print_order():
    if(x.get() ==0):
        print('you ordered Apple')
    elif (x.get() == 1):
        print('you ordered Orange')
    elif (x.get() ==2):
        print('You ordered Banana')
    elif (x.get() ==3):
        print('You ordered Guava')
    else:
        print('you orderd Mango')

fruids_name=['Apple','Orange','Banana','Guava','Mango']
x=IntVar()

for index in range(len(fruids_name)):
    radio_button=Radiobutton(w,
                             text=fruids_name[index],
                             variable=x,
                             value=index,
                             command=print_order,
                             background='lightgray',
                             border=5,

                             )
    radio_button.pack(anchor=SW)

scale=Scale(w,
            from_=0,
            to=100,
            orient=HORIZONTAL,
            )
scale.pack(anchor=W)



w.mainloop()
