import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    if length <= 0:
        messagebox.showwarning("Invalid Length", "Password length should be greater than 0.")
        return

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase + uppercase + digits + symbols

    password = ''.join(random.choice(all_characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and Entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root, width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Entry to display the generated password
password_entry = tk.Entry(root, width=20)
password_entry.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()