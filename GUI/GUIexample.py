import tkinter

screen = tkinter.Tk()
# w *  h
screen.geometry("500x500")
screen.configure(bg="grey")

#tkinter variable
var_ename_id = tkinter.StringVar()  #it will accept value in string.
var_num = tkinter.IntVar()

def myfun():
    print("welcome")
    print("value from entry = ",var_ename_id.get())


#label
lbl = tkinter.Label(screen,text="welcome to tkinter",font=("arial","26","bold"),bg="grey")
lbl.place(x=80,y=10)

#label
lbl_name = tkinter.Label(screen,text="enter your name : ",font=("arial","10","bold"),bg="grey")
lbl_name.place(x=20,y=80)

#entry
e1 = tkinter.Entry(screen,textvariable=var_ename_id)
e1.place(x=160,y=80)

#button

btn = tkinter.Button(screen,text="Submit",font=("arial","10","bold"),command=myfun)
btn.place(x=300,y=80)

screen.mainloop()