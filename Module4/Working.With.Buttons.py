from tkinter import *

def update_color():
    if window.cget("bg") == "lightgray":
        window.configure(bg="lightpink")
    else:
        window.configure(bg="lightgray")

window = Tk()
window.title("Working with buttons")
window.geometry("900x600")
window.configure(bg="lightgray")
btn_update = Button(window, text="Update color", command=update_color)
btn_update.place(x=20, y=20)
btn_exit = Button(window, text="Exit", command="exit")
btn_exit.place(x=120, y=20)
window.mainloop()
