from tkinter import *
from math import log

root = Tk()
root.title("Press btn?")



def log_calu():
    
    logs = Toplevel()
    logs.title("Log_calu?")

    e = Entry(logs, borderwidth=8, border=8)
    e.grid(column=0, row=1, columnspan=3)
    e.insert(0, "Enter b: ")


    def num(number):
        e.insert(END, number)

    def dec():

        num = str(e.get())
        e.delete(0, END)
        num1 = num + ","
        e.insert(0, num1)

    def res():
        global reset
        e.delete(0, END)
        e.insert(0, "Enter b: ")
        reset.destroy()
        enter = Button(logs, text="ENT", command=ent)
        enter.grid(column=2, row=5)


    def ent():
        global reset
        global num1
        ent = str(e.get())

        if "b:" in ent:
            num1 = e.get() + " "
            num1 = num1[9:-1]
            print(num1)
            e.delete(0, END)
            e.insert(0, "Enter n: ")
        elif "n:" in ent:
            num2 = e.get() + " "
            num2 = num2[9:-1]
            print(num2 + "HW")
            e.delete(0, END)
            num3 = log(float(num1), float(num2))
            e.insert(0,num3)
            enter.destroy()
            reset = Button(logs, text="RES", command=res)
            reset.grid(row=5, column=2)
        else:
            print("NA")



    log_label = Label(logs, text="logb(n)")
    log_label.grid(column=0, row=0, columnspan=3)

    num1 = Button(logs, text="1", command=lambda: num(1))
    num2 = Button(logs, text="2", command=lambda: num(2))
    num3 = Button(logs, text="3", command=lambda: num(3))
    num4 = Button(logs, text="4", command=lambda: num(4))
    num5 = Button(logs, text="5", command=lambda: num(5))
    num6 = Button(logs, text="6", command=lambda: num(6))
    num7 = Button(logs, text="7", command=lambda: num(7))
    num8 = Button(logs, text="8", command=lambda: num(8))
    num9 = Button(logs, text="9", command=lambda: num(9))
    num0 = Button(logs, text="0", command=lambda: num(0))
    decimal = Button(logs, text=",", command= dec)

    enter = Button(logs, text="ENT", command=ent)


    num1.grid(column=0, row=4)
    num2.grid(column=1, row=4)
    num3.grid(column=2, row=4)

    num4.grid(column=0, row=3)
    num5.grid(column=1, row=3)
    num6.grid(column=2, row=3)

    num7.grid(column=0, row=2)
    num8.grid(column=1, row=2)
    num9.grid(column=2, row=2)

    num0.grid(column=1, row=5)
    decimal.grid(column=0, row=5)

    enter.grid(column=2, row=5)




    logs.mainloop()

log_btn = Button(root, text="log", padx=10, pady=10, command=log_calu).pack()

root.mainloop()
