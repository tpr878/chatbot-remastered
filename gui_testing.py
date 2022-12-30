import tkinter  
from tkinter import * 
from tkinter.ttk import *

root = tkinter.Tk()
root.title('हिंदी चैटबॉट')
root.configure(bg = 'white')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('{}x{}'.format(screen_width, screen_height))
root.state('zoomed')

photo = PhotoImage(file = r"C:\Users\kamra\Documents\AIIT\Chatbot Remastered\remove.png")
btn = Button(root, image = photo)


# btn.pack(side=BOTTOM)
btn.pack(side=BOTTOM, padx=(screen_width-65, 10), pady=(screen_height-150, 10))


root.mainloop()


