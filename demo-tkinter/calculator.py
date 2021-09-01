import parser
from tkinter import *

root = Tk()
root.title('Calculator')

index = 0


# get user input
def get_input(number):
    global index
    display.insert(index, number)
    index += 1


# clear input
def clear_all():
    display.delete(0, END)


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        display.insert(0, "error")
        clear_all()


# get operation
def get_operation(operator):
    global index
    length = len(operator)
    display.insert(index, operator)
    index += length


# calculate
def calculate():
    entire_string = display.get()
    try:
        str = parser.expr(entire_string).compile()
        result = eval(str)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "error")


# add input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

# add number buttons
Button(root, text="1", command=lambda: get_input(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_input(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_input(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: get_input(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_input(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_input(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: get_input(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_input(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_input(9)).grid(row=4, column=2)

# add operator buttons
Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_input(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3)

Button(root, text="pi", command=lambda: get_operation("*3.14")).grid(row=2, column=4)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", command=lambda: get_operation("**")).grid(row=5, column=4)

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5)
Button(root, text="x!").grid(row=3, column=5)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5)
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5)

root.mainloop()
