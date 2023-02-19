from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import time
from matplotlib import pyplot as plt
import re


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
        with open(filepath, encoding='utf-8') as file:
            text = file.read().upper()
            text = re.sub(r'[.,"\'-?:!;«»—\n]', '', text)
            text = text.replace("Ё", "Е")
            text_editor1.delete("1.0", END)
            text_editor1.insert("1.0", text)
            text_editor1.get(1.0, END)



root = Tk()
root.title("Лабораторная работа №2")
root.geometry("1300x900")
tab_control = ttk.Notebook(root)

# first page Affine Chipper
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Шифр Цезаря")

#Var
value_a = StringVar()

# Add Element on Layer First Page
original_text_label = Label(tab1, text="Исходный текст:")
encrypted_text_label = Label(tab1, text="Зашифрованный текст:")
decrypted_text_label = Label(tab1, text="Расшифрованный текст:")
time_enc_chipper = Label(tab1, text= "Время зашифрования")
time_dec_chipper = Label(tab1, text= "Время расшифрования")
text_editor1 = Text(tab1)
open_file_button = Button(tab1, text="Открыть файл",)
endec_button_affine = Button(tab1, text="Выполнить")
text_editor2 = Text(tab1)
text_editor3 = Text(tab1)

def time_of_function1(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        time_enc_chipper['text'] = f"{(time.perf_counter_ns() - start_time) / 10**6} мс"
        return res

    return wrapped

def time_of_function2(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        time_dec_chipper['text'] = f"{(time.perf_counter_ns() - start_time)/ 10 ** 6} мс"
        return res

    return wrapped


@time_of_function1
def affine_encrypt(text, key):
    return ''.join([chr(((key[0] * (ord(t) - ord('А')) + key[1]) % 33) + ord('А')) for t in text.upper().replace(' ', '')])
@time_of_function2
def affine_decrypt(cipher, key):
    return ''.join([chr(((modinv(key[0], 33) * (ord(c) - ord('А') - key[1])) % 33) + ord('А')) for c in cipher])


# Main Function
def main(event):
    key = [7, 10]
    def get_text():
       return text_editor1.get(1.0, END).upper()

    def insert_text_2(text):
        text = text
        return text_editor2.insert(1.0, text)

    def get_text_1():
        return text_editor1.get(1.0, END).upper()

    def get_text_2():
        return text_editor2.get(1.0, END).upper()

    def insert_text_3(text):
        text = text
        return text_editor3.insert(1.0, text)

    affine_encrypted_text = affine_encrypt(get_text(), key)
    affine_decrypted_text = affine_decrypt(get_text_2(), key)

# Output data in vidget
    insert_text_2(affine_encrypted_text)
    insert_text_3(affine_decrypted_text)

# Drawing Gistograms
    txt_en_cez = list(affine_encrypted_text)
    n_bin1_cez = len(set(txt_en_cez))
    s1 = plt.hist(txt_en_cez, bins=n_bin1_cez, density=True, align='mid')
    plt.suptitle("Для зашифрованного")
    plt.grid(which='major')
    plt.rcParams['patch.force_edgecolor'] = True
    plt.show()

    txt_dec_cez = list(get_text_1())
    n_bin2_cez = len(set(txt_dec_cez))
    s2 = plt.hist(txt_dec_cez, bins=n_bin2_cez, density=True, align='mid')
    plt.suptitle("Для исходного")
    plt.grid(which='major')
    plt.rcParams['patch.force_edgecolor'] = True
    plt.show()

# Drawing all elements
original_text_label.grid(row=0, column=0)
encrypted_text_label.grid(row=2, column=0)
decrypted_text_label.grid(row=2, column=1)
open_file_button.bind('<Button-1>', open_file)
endec_button_affine.bind('<Button-1>', main)
text_editor1.grid(row=1, column=0)
text_editor2.grid(row=3,column=0)
text_editor3.grid(row=3,column=1)
open_file_button.grid(row=0, column=1)
time_enc_chipper.grid(row=4, column=0)
time_dec_chipper.grid(row=4, column=1)
endec_button_affine.grid(row=5, column=0)
tab_control.pack(expand=1, fill="both")
root.mainloop()
