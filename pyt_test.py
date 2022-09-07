from tkinter import *

root = Tk()
root.title("Test_pyt")

pyt = False

def button_num(number):
    e.insert(END, number)

def button_pyt():
    global pyt
    if pyt == False:
        global run
        e.delete(0,END)
        e.insert(0, "Enter first num: ")
        pyt = True



def button_ent():
    global pyt
    global num1
    if pyt == True:
        num1 = e.get() + " "
        num1 = float(num1[17:-1])
        e.delete(0, END)
        e.insert(0, "Enter second num: ")
        pyt = False
    elif pyt == False:
        num2 = e.get() + " "
        e.delete(0,END)
        num2 = float(num2[18:-1])
        num3 = str((num1**2 + num2**2)**(1/2))
        e.insert(0, num3)




# Define buttons

e = Entry(root, width=20, borderwidth=10)

# numpad
button_1 = Button(root, text="1", padx=20, pady=10,
                  command=lambda: button_num(1))
button_2 = Button(root, text="2", padx=20, pady=10,
                  command=lambda: button_num(2))
button_3 = Button(root, text="3", padx=20, pady=10,
                  command=lambda: button_num(3))
button_4 = Button(root, text="4", padx=20, pady=10,
                  command=lambda: button_num(4))
button_5 = Button(root, text="5", padx=20, pady=10,
                  command=lambda: button_num(5))
button_6 = Button(root, text="6", padx=20, pady=10,
                  command=lambda: button_num(6))
button_7 = Button(root, text="7", padx=20, pady=10,
                  command=lambda: button_num(7))
button_8 = Button(root, text="8", padx=20, pady=10,
                  command=lambda: button_num(8))
button_9 = Button(root, text="9", padx=20, pady=10,
                  command=lambda: button_num(9))
button_0 = Button(root, text="0", padx=20, pady=10,
                  command=lambda: button_num(0))

button_pyt = Button(root, text="pyt", padx=10, pady=10,
                    command= button_pyt)
button_ent = Button(root, text="ent", padx=10, pady=10,
                    command= button_ent)


# Put buttons on screen

button_1.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=0)
button_4.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=0)
button_7.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=0)
button_0.grid(row=4, column=1)

button_pyt.grid(row=1, column=3)
button_ent.grid(row=2, column=3)
e.grid(row=0, column=0, columnspan=3)




root.mainloop()