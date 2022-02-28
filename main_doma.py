import random
from tkinter import *

num = range(0,50)


def submt(var1):
    if var1.get() == str(plus()):
        spravne = Label(app, text="Správně", fg="green", font=("Courier", 16))
        spravne.place(relx=0.3, rely=0.2)
    else:
        spatne = Label(app, text="Špatně", fg="red", font=("Courier", 16))
        spatne.place(relx=0.3, rely=0.2)


def Zkus_znovu():
    Zkus_znovu.num1update = random.choice(num)
    Zkus_znovu.num2update = random.choice(num)
    newQ = Label(
        app, text=f"{Zkus_znovu.num1update}+{Zkus_znovu.num2update}", font=("Courier", 16)
    )
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def plus():
    Zkus_znovu
    return Zkus_znovu.num1update + Zkus_znovu.num2update

def krat(self):
    zkus_znovu
    return zkus_znovu.num1update * zkus_znovu.num2update

def deleno(self):
    zkus_znovu
    return zkus_znovu.num1update / zkus_znovu.num2update


def minus(self):
    zkus_znovu
    return zkus_znovu.num1update - zkus_znovu.num2update


app = Tk()
app.title("Matematika")

app.geometry("240x300")
app.resizable(False, False)
start = Button(app, text="Start", command=Zkus_znovu)
start.place(relx=0.45, rely=0.2)

solving = Entry(app)
solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)
submit = Button(app, text="kontrola", command=lambda: submt(solving))
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)
Zkus_znovu = Button(app, text="Další příklad", command=Zkus_znovu)
Zkus_znovu.place(relx=0.39, rely=0.9)
app.mainloop()