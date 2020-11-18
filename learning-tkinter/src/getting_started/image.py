from tkinter import *

root = Tk()

frames = [PhotoImage(file='Slidercrank_animation.gif',format = 'gif -index %i' %(i)) for i in range(30)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == 30:
        ind = 0
    label.configure(image=frame)
    root.after(30, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()
