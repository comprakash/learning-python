from tkinter import *
from tkinter import ttk

root = Tk()

Label(root, text='Hello, Om!').pack()

button = ttk.Button(root, text='Click Me')
button.pack()

button['text'] = 'Press Me'
button.config(text='Push Me')

print(button)
print(root)

root.mainloop()
