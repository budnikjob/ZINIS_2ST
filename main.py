from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# Help Function
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def open_file(event):
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)


root = Tk()
root.title("Лабораторная работа №2")
root.geometry("1024x720")
tab_control = ttk.Notebook(root)

# first page Affine Chipper
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Шифр Цезаря")

# Add Element on Layer First Page
original_text_label = Label(tab1, text="Исходный текст:")
text_editor = Text(tab1)
open_file_button = Button(tab1, text="Открыть файл",)



# Main Function
def main(event):
    pass

# Drawing all elements
original_text_label.grid(row=0, column=0)
open_file_button.bind('<Button-1>', open_file)
open_file_button.grid(row=0, column=1)
text_editor.grid(row=1, column=0)
tab_control.pack(expand=1, fill="both")
root.mainloop()
