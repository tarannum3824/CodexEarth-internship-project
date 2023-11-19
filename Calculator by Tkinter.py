import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()

# Entry widget for display
entry = tk.Entry(root, width=16, font=('Arial', 20), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Special case for the '=' button
tk.Button(root, text='=', width=5, height=2, command=calculate).grid(row=5, column=0, columnspan=4)

# Special case for the 'C' button to clear the entry
tk.Button(root, text='C', width=5, height=2, command=clear_entry).grid(row=6, column=0, columnspan=4)

# Run the main loop
root.mainloop()