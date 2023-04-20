from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x200")
window.title("Text Input App")

lbl = Label(window, text="Process Text!")
lbl.pack()

txt_input = Text(window, height = 5, width = 52)
txt_input.pack()

def msg_alert():
    messagebox.showinfo("Message",txt_input.get(1.0, "end-1c"))


btn_warn = Button(window, text="Show Message", command=msg_alert)
btn_warn.pack()

btn_close = Button(window, text="Exit", command=window.destroy)
btn_close.pack()

window.mainloop()
