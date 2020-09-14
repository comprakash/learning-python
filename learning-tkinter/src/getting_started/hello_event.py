from tkinter import *
from tkinter import ttk


class HelloApp:
    def __init__(self, master):
        self.label = ttk.Label(master, text="Hello, Tkinter!")
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text="Bengaluru", command=self.hello).grid(row=1, column=0)

    def hello(self) -> None:
        self.label.config(text="Howdy, Bengaluru")


def main():
    root = Tk()
    HelloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
