from tkinter import *
from tkinter import ttk, filedialog

# Create a window
root = Tk()
root.title("SCR Software Onboarding 2024")
#root.geometry("800x800")
# cargo cults from https://tkdocs.com/tutorial/firstexample.html cutely
real_root = ttk.Frame(root, padding="16 16 16 16")
real_root.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# TODO: Create a label that shows "Hello, SCR!"
ttk.Label(real_root, text="Hello, SCR!").grid(column=0, row=0)
# TODO: Create a button that prints "Hello, SCR!" to the console.
def greet_scr():
    print("Hello, SCR!")
ttk.Button(real_root, text="👋", command=greet_scr).grid(column=1, row=0)
# TODO: Create a text box that allows the user to type in their name. Add a button that prints "Hello, <name>!" to the console.
name = StringVar()
name_entry = ttk.Entry(real_root, width=10, textvariable=name)
name_entry.grid(column=0, row=1)
def greet_user():
    print(f"Hello, {name.get()}!")
ttk.Button(real_root, text="Greet", command=greet_user).grid(column=1, row=1)
# TODO: Create a file dialog that allows the user to select a file. Print the file path to the console.
def ask_file():
    print(filedialog.askopenfilename())
ttk.Button(real_root, text="Look up file", command=ask_file).grid(column=0, row=2)
# Show the window (loop)
root.mainloop()