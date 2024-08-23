import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        messagebox.showinfo("Generated Password", f"Your Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
