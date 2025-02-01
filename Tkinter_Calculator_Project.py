from tkinter import *

# Initialize the main window
window = Tk()
window.title("Calculator")
window.geometry("312x324")
window.resizable(0, 0)

# Global variable to hold the expression
expression = ""
input_text = StringVar()

# Functions
def btn_click(item):
    """Handles button clicks and appends input to the expression."""
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    """Clears the input field."""
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    """Evaluates the expression and displays the result."""
    global expression
    try:
        result = str(eval(expression))  # Evaluate the mathematical expression
        input_text.set(result)
        expression = result  # Store result for further calculations
    except:
        input_text.set("Error")  # Handle invalid expressions
        expression = ""

# UI Design
input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=("arial", 15, "bold"), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btn_frame = Frame(window, width=312, height=272.5, bg="grey")
btn_frame.pack()

# Button Layout
buttons = [
    ('C', 0, 0, 3, btn_clear), ('/', 0, 3, 1, lambda: btn_click("/")),
    ('7', 1, 0, 1, lambda: btn_click(7)), ('8', 1, 1, 1, lambda: btn_click(8)), ('9', 1, 2, 1, lambda: btn_click(9)), ('*', 1, 3, 1, lambda: btn_click("*")),
    ('4', 2, 0, 1, lambda: btn_click(4)), ('5', 2, 1, 1, lambda: btn_click(5)), ('6', 2, 2, 1, lambda: btn_click(6)), ('-', 2, 3, 1, lambda: btn_click("-")),
    ('1', 3, 0, 1, lambda: btn_click(1)), ('2', 3, 1, 1, lambda: btn_click(2)), ('3', 3, 2, 1, lambda: btn_click(3)), ('+', 3, 3, 1, lambda: btn_click("+")),
    ('0', 4, 0, 2, lambda: btn_click(0)), ('.', 4, 2, 1, lambda: btn_click(".")), ('=', 4, 3, 1, btn_equal)
]

# Dynamically create buttons
for (text, row, col, colspan, command) in buttons:
    Button(btn_frame, text=text, fg="black", width=10 * colspan, height=3, bd=0, bg="#fff", cursor="hand2", command=command)\
        .grid(row=row, column=col, columnspan=colspan)

# Start the main event loop
window.mainloop()
