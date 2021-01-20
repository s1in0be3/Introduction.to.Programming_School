from tkinter import *

window = Tk()
window.title("Hello world, in a window")
window.geometry("900x600")
label = Label(window, text="HELLO WORLD")
label.pack(padx=200, pady=50)
window.mainloop()
