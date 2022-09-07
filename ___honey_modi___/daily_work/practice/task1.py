import tkinter

screen = tkinter.Tk()
screen.geometry("500x500")
screen.configure(bg="black")

#tkinter variable
var_ename_id = tkinter.StringVar()  #it will accept value in string.
# var_num = tkinter.IntVar()
count = 0

def like():
    global count
    print("welcome")
    count += 1
    # mLabel = tkinter.Label(screen, text=count).pack()
    print("value from entry = ",count)

def dislike():
    global count
    # print("welcome")
    count -= 1
    # mLabel = tkinter.Label(screen, text=count).pack()
    print("value from entry = ",count)

#label
lbl = tkinter.Label(screen,text="welcome to tops",font=("arial","15","bold"),bg="white")
lbl.place(x=150,y=40)

#labelname
lbl_name = lbl_name = tkinter.Label(screen,text="Total like :",font=("arial","10","bold"),bg="white")
lbl_name.place(x=20,y=80)

#button
btn = tkinter.Button(screen,text="Like",font=("arial","10","bold"),command=like)
btn.place(x=120,y=80)

#button
btn = tkinter.Button(screen,text="Dislike",font=("arial","10","bold"), command=dislike)
btn.place(x=250,y=80)

screen.mainloop()