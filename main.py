from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Лабораторная работа №2")
root.geometry("1024x720")
tab_control = ttk.Notebook(root)

#first page Affine Chipper
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Шифр Цезаря")




tab_control.pack(expand=1, fill="both")
root.mainloop()