import tkinter as tk

root = tk.Tk()
root.title('हिंदी चैटबॉट')
root.configure(bg = 'white')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('{}x{}'.format(screen_width, screen_height))
root.state('zoomed')



root.mainloop()
