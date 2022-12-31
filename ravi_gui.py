import tkinter as tk 
from tkinter import *
from tkinter.ttk import *

root = tk.Tk()
root.title('हिंदी चैटबॉट')
root.configure(bg = 'white', borderwidth = 0)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('{}x{}'.format(screen_width, screen_height))
root.state('zoomed')

#buttons stuff
photo_end = PhotoImage(file = r"E:\Chatbot remastered\remove.png")
photo_send = PhotoImage(file = r"E:\Chatbot remastered\send-message.png")

btn_end = tk.Button(root, image = photo_end, borderwidth = 0, bg = 'white')
btn_send = tk.Button(root, image = photo_send, borderwidth = 0, bg = 'white')

btn_end.place(x=1865, y=990)
btn_send.place(x=1812, y=990)

#textfield stuff
textfield = Text(root, relief=RIDGE, bg='white',height = 1.5, width = 119, borderwidth=2, font=('Helvatical bold',20), pady = 0, padx = 2)
textfield.place(x=12, y=975)



root.mainloop()


