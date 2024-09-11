from tkinter import *

# function to calculate values
def calculate():
    try:
        expression  = entry.get()
        result = eval(expression)
        entry.delete(0,END)     
        entry.insert(END, str(int(result)) if result == int(result) else str(result))
    except Exception:
        entry.delete(0,END)
        entry.insert(END, "Error")
     
# function to clear entry      
def clear_entry():
    entry.delete(0,END)

# function to display text into entry widget
def button_click(value):
    current_value = entry.get()
    entry.delete(0,END)
    entry.insert(END, current_value + str(value))

# GUI window
root = Tk() 
root.title("Calculator")

entry = Entry(root, font=('Arial', 20), bd=8, width=15, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# list of buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '+',
    'C', '0', '-', '='
]

# Creating buttons 
row = 1
col = 0
for button in buttons:
    if button == "=":
        Button(root, text = button, font=('Arial', 10), padx=20, pady=20,
               command = calculate).grid(row = row, column = col, columnspan=2)
        col += 2
    elif button == "C":
        Button(root, text = button, font=('Arial', 10), padx=20, pady=20,
               command = clear_entry).grid(row = row, column = col)
        col += 1
    else:
        Button(root, text = button, font=('Arial', 10), padx=20, pady=20, 
               command = lambda b=button: button_click(b)).grid(row = row, column = col)  
        col += 1
    
    # Move buttons to the next row after every 4 buttons   
    if col>3:
        col = 0
        row += 1
        

root.mainloop()