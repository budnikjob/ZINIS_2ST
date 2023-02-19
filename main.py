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
        with open(filepath,encoding='utf-8') as file:
            text = file.read()
            text_editor1.delete("1.0", END)
            text_editor1.insert("1.0", text)
            text_editor1.get(1.0, END)

def affine_encrypt(text, key):
    return ''.join([chr(((key[0] * (ord(t) - ord('А')) + key[1]) % 33)
                        + ord('А')) for t in text.upper().replace(' ', '')])

root = Tk()
root.title("Лабораторная работа №2")
root.geometry("1500x720")
tab_control = ttk.Notebook(root)

# first page Affine Chipper
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Шифр Цезаря")

#Var
value_a = StringVar()

# Add Element on Layer First Page
original_text_label = Label(tab1, text="Исходный текст:")
encrypted_text_label = Label(tab1, text="Зашифрованный текст:")
text_editor1 = Text(tab1)

open_file_button = Button(tab1, text="Открыть файл",)
endec_button_affine = Button(tab1, text="Выполнить")
text_editor2 = Text(tab1)


# Main Function
def main(event):
    key = [7, 10]
    def get_text():
       return text_editor1.get(1.0, END).upper()

    def insert_text_2(text):
        text = text
        return text_editor2.insert(1.0, text)

    affine_encrypted_text = affine_encrypt(get_text(), key)


# Output data in vidget
    insert_text_2(affine_encrypted_text)
# Drawing all elements
original_text_label.grid(row=0, column=0)
encrypted_text_label.grid(row=0, column=1)
open_file_button.bind('<Button-1>', open_file)
endec_button_affine.bind('<Button-1>', main)
text_editor1.grid(row=1, column=0)
text_editor2.grid(row=1,column=1)
open_file_button.grid(row=0, column=2)
endec_button_affine.grid(row=2, column=0)
tab_control.pack(expand=1, fill="both")
root.mainloop()
