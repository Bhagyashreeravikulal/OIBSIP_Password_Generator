# Random Password Generator with GUI
# BCA Mini Project

import tkinter as tk
from tkinter import messagebox
import random
import string

# -----------------------------
# Password Generation Function
# -----------------------------
def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return

        characters = ""

        if var_letters.get():
            characters += string.ascii_letters

        if var_numbers.get():
            characters += string.digits

        if var_symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one character type")
            return

        password = ""

        for i in range(length):
            password += random.choice(characters)

        password_output.delete(0, tk.END)
        password_output.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter valid number for length")


# -----------------------------
# Copy to Clipboard
# -----------------------------
def copy_password():
    password = password_output.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate a password first")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard")


# -----------------------------
# Clear Fields
# -----------------------------
def clear_fields():
    length_entry.delete(0, tk.END)
    password_output.delete(0, tk.END)

    var_letters.set(0)
    var_numbers.set(0)
    var_symbols.set(0)


# -----------------------------
# Application Window
# -----------------------------
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("450x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# -----------------------------
# Password Length Input
# -----------------------------
length_frame = tk.Frame(root)
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5)

length_entry = tk.Entry(length_frame)
length_entry.grid(row=0, column=1, padx=5)

# -----------------------------
# Character Options
# -----------------------------
options_frame = tk.Frame(root)
options_frame.pack(pady=15)

var_letters = tk.IntVar()
var_numbers = tk.IntVar()
var_symbols = tk.IntVar()

letters_check = tk.Checkbutton(options_frame, text="Letters (A-Z, a-z)", variable=var_letters)
letters_check.pack(anchor="w")

numbers_check = tk.Checkbutton(options_frame, text="Numbers (0-9)", variable=var_numbers)
numbers_check.pack(anchor="w")

symbols_check = tk.Checkbutton(options_frame, text="Symbols (!@#$)", variable=var_symbols)
symbols_check.pack(anchor="w")

# -----------------------------
# Generate Button
# -----------------------------
generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="green",
    fg="white",
    width=20
)
generate_button.pack(pady=10)

# -----------------------------
# Output Field
# -----------------------------
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

output_label = tk.Label(output_frame, text="Generated Password:")
output_label.grid(row=0, column=0)

password_output = tk.Entry(output_frame, width=30)
password_output.grid(row=0, column=1)

# -----------------------------
# Buttons Frame
# -----------------------------
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=20)

copy_button = tk.Button(
    buttons_frame,
    text="Copy",
    command=copy_password,
    width=10
)
copy_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    buttons_frame,
    text="Clear",
    command=clear_fields,
    width=10
)
clear_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(
    buttons_frame,
    text="Exit",
    command=root.quit,
    width=10
)
exit_button.grid(row=0, column=2, padx=10)

# -----------------------------
# Footer
# -----------------------------
footer = tk.Label(
    root,
    text="BCA Mini Project - Python Password Generator",
    font=("Arial", 9)
)
footer.pack(side="bottom", pady=10)

# -----------------------------
# Run Application
# -----------------------------
root.mainloop()
