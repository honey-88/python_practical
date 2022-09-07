from random import random
import tkinter

screen=tkinter.TK()
screen.title("ROCK PAPER SCISSOR")
screen.geometry("500*500")

var_user_choice=tkinter.Stringvar()
var_com_choice=tkinter.Stringvar()
game_list=["ROCK","PAPER","SCISSOR"]

def myfun(msg):
    var_user_choice(msg)
    com=random.choice(game_list)
    var_com_choice.set(com)

    if msg==com:
        var_result_choice.set("TIE")

    else:
        if msg=="ROCK"and com=="PAPER":
            var_result_choice.set("COMPUTER won")

            if choice==1:

                choice_name='rock'
            elif choice==2:

                choice_name='paper' 
            else:

                choice_name='scissor'





btn=tkinter.Button(screen,text="ROCK",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lamda:myfun("ROCK"))
btn.place(x=10,y=10)

btn=tkinter.Button(screen,text="PAPER",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lamda:myfun("PAPER")))
btn.place(x=150,y=10)

btn=tkinter.Button(screen,text="SCISSOR",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lamda:myfun("SCISSOR")))
btn.place(x=330,y=10)


user=tkinter.Label(screen,text="USER",font=('arial',14,'bold'))
user.place(x=10,y=150)

computer=tkinter.Label(screen,text="COMPUTER",font=('arial',14,'bold'))

computer.place(x=10,y=200)

user=tkinter.Label(screen,text="ROCK",font=('arial',14,'bold'))
user.place(x=150,y=150)

computer=tkinter.Label(screen,text="ROCK",)

btn=tkinter.Button(screen,textvariable=var_result_choice,font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforground="white",width="25")

btn.place(x=10,y=400)
screen.mainloop()