# Simple Password Generator
# Author: Jędrzej Bakalarski
# Github: https://github.com/jedrzejme/SimplePasswordGenerator

# Import libraries
import random
import string
import tkinter as tk
from tkinter import messagebox
import webbrowser

# Define function for generating password
def generate_password(length, uppercase, lowercase, digits, special):
    all_characters = ""
    if uppercase:
        all_characters += string.ascii_uppercase
    if lowercase:
        all_characters += string.ascii_lowercase
    if digits:
        all_characters += string.digits
    if special:
        all_characters += string.punctuation

    if not all_characters:
        raise ValueError("You must select at least one character type!")

    password = "".join(random.choice(all_characters) for _ in range(length))
    return password

# Define functions for GUI
def on_generate():
    try:
        length = int(entry_length.get())
        uppercase = var_uppercase.get()
        lowercase = var_lowercase.get()
        digits = var_digits.get()
        special = var_special.get()
        
        password = generate_password(length, uppercase, lowercase, digits, special)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Define function for copying password to clipboard
def copy_to_clipboard():
    try:
        root.clipboard_clear()
        root.clipboard_append(entry_password.get())
        root.update()
    except Exception as e:
        messagebox.showerror("Error", f"Could not copy to clipboard: {str(e)}")

# Define opening web version
def OpenWebVersion():
    webbrowser.open_new("https://simple-password-generator.jbs.ovh/")

# Define opening source code
def OpenSupportMe():
    webbrowser.open_new("https://support.jedrzej.me/")

# Creating the main application window
root = tk.Tk()
root.title("Simple Password Generator")
root.geometry("330x380")
root.resizable(False, False)
root.iconbitmap("icon.ico")

# Setting the dark theme colors
bg_color = "#2e2e2e"
fg_color = "#ffffff"
button_color = "#414141"
entry_bg_color = "#3e3e3e"
root.configure(bg=bg_color)

# Adding widgets to the window
tk.Button(root, text="Web Version", command=OpenWebVersion, bg=button_color, fg=fg_color).grid(row=0, column=0, columnspan=2, padx=10, pady=10)
tk.Button(root, text="Support Me", command=OpenSupportMe, bg=button_color, fg=fg_color).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Password length:", bg=bg_color, fg=fg_color).grid(row=2, column=0, padx=10, pady=10)
entry_length = tk.Entry(root, bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
entry_length.grid(row=2, column=1, padx=10, pady=10)

var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase letters", variable=var_uppercase, bg=bg_color, fg=fg_color, selectcolor=button_color).grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Lowercase letters", variable=var_lowercase, bg=bg_color, fg=fg_color, selectcolor=button_color).grid(row=3, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Digits", variable=var_digits, bg=bg_color, fg=fg_color, selectcolor=button_color).grid(row=4, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Special characters", variable=var_special, bg=bg_color, fg=fg_color, selectcolor=button_color).grid(row=4, column=1, padx=10, pady=5, sticky="w")

tk.Button(root, text="Generate", command=on_generate, bg=button_color, fg=fg_color).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Generated password:", bg=bg_color, fg=fg_color).grid(row=6, column=0, padx=10, pady=10, sticky="w")
entry_password = tk.Entry(root, width=50, bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
entry_password.grid(row=7, column=0, padx=10, pady=10, sticky="e", columnspan=2)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg=button_color, fg=fg_color).grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Starting the main application loop
root.mainloop()
