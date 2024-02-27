from tkinter import *
w=Tk()

w.geometry("520x520")
w.title("Student Management System")
w.config(background='lightgray')

def submit():
    username=entry.get()
    print(username)

def delete():
    entry.delete(0, END)

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
w.mainloop()
