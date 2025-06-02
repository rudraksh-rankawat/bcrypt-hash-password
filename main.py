import bcrypt
import tkinter as tk


def validate(input_pass):
    input_pass: str = entry.get()
    if bcrypt.checkpw(input_pass.encode(encoding="utf-8"), b'$2b$12$18sEMovCdImHXNulYR3AzuEticaw7uUU14z6eZaq2.XJmwvYE2i5m'):
        print("login successful")
        label.config(text="Login Successful")
    else:
        print("incorrect password")
        label.config(text="Incorrect Password")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Login", command=lambda: validate(entry.get()))
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()


# used this to generate hashed password
# password = b"notrevealingyet"
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
