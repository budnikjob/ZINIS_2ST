from tkinter import *
import time
from itertools import cycle
from matplotlib import pyplot as plt
from tkinter import ttk
from tkinter import filedialog


alp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
root = Tk()
root.title("Лабораторная работа №2")
root.geometry("600x200")
root.resizable(width=False, height=False)

value_textNEN = StringVar()

value_textNEN_Viz = StringVar()
value_KEY_Viz = StringVar()

label_NAME_CEZ = Label(text="Шифр Цезаря")
label1 = Label(text="Ваш текст:")
entry1 = Entry(textvariable= value_textNEN)
ok_button1 = Button(text="Найти")
label2 = Label(text="Зашифрованный текст:")
label2_1 = Label(text="Время шифрования")
label3 = Label(text="Расшифрованный текст:")
label3_1 = Label(text="Время расшифрования")


label_NAME_VIZ = Label(text="Шифр Вижинера")
label_text_1 = Label(text="Ваш текст:")
entry_text_1 = Entry(textvariable=value_textNEN_Viz)
label_text_2 = Label(text="Ваш ключ:")
entry_text_2 = Entry(textvariable=value_KEY_Viz)

en_text_1_viz = Label(text="Зашифрованный текст:")
out_en_viz =  Label()

dec_text_1_viz = Label(text="Расшифрованный текст:")
out_dec_viz = Label()

time_viz_1 = Label(text="Время шифрования")
time_viz_2 = Label(text="Время дешифрования")



Decrypted_output = Label()
Encrypt_output = Label()

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

def main(event):
    a = value_textNEN.get().upper()
    b = value_textNEN_Viz.get().upper()
    c = value_KEY_Viz.get().upper()
    print(a)
    key = [7, 10]
    def time_of_function1(function):
        def wrapped(*args):
            start_time = time.perf_counter_ns()
            res = function(*args)
            label3_1['text'] = f"{(time.perf_counter_ns() - start_time)} мс"
            return res
        return wrapped
    def time_of_function2(function):
        def wrapped(*args):
            start_time = time.perf_counter_ns()
            res = function(*args)
            label2_1['text'] = f"{(time.perf_counter_ns() - start_time)} мс"
            return res
        return wrapped

    def time_of_function3(function):
        def wrapped(*args):
            start_time = time.perf_counter_ns()
            res = function(*args)
            time_viz_1['text'] = f"{(time.perf_counter_ns() - start_time)} мс"
            return res
        return wrapped

    def time_of_function4(function):
        def wrapped(*args):
            start_time = time.perf_counter_ns()
            res = function(*args)
            time_viz_2['text'] = f"{(time.perf_counter_ns() - start_time)} мс"
            return res
        return wrapped

    @time_of_function3
    def encode_vijn(text, keytext):
        f = lambda arg: alp[(alp.index(arg[0]) + alp.index(arg[1]) % 33) % 33]
        return ''.join(map(f, zip(text, cycle(keytext))))

    @time_of_function4
    def decode_vijn(coded_text, keytext):
        f = lambda arg: alp[alp.index(arg[0]) - alp.index(arg[1]) % 33]
        return ''.join(map(f, zip(coded_text, cycle(keytext))))


    @time_of_function1
    def affine_decrypt(cipher, key):
        return ''.join([chr(((modinv(key[0], 33) * (ord(c) - ord('А') - key[1]))
                             % 33) + ord('А')) for c in cipher])
    @time_of_function2
    def affine_encrypt(text, key):
        return ''.join([chr(((key[0] * (ord(t) - ord('А')) + key[1]) % 33)
                            + ord('А')) for t in text.upper().replace(' ', '')])

    out_en_viz['text'] = encode_vijn(b, c)
    encode_viz = encode_vijn(b, c)
    out_dec_viz['text'] = decode_vijn(encode_viz, c)
    affine_encrypted_text = affine_encrypt(a, key)
    Encrypt_output['text'] = affine_encrypted_text
    Decrypted_output['text'] = affine_decrypt(affine_encrypted_text, key)

    txt_en_cez = list(affine_encrypted_text)
    n_bin1_cez = len(set(txt_en_cez))
    s1 = plt.hist(txt_en_cez, bins=n_bin1_cez)
    plt.rcParams['patch.force_edgecolor'] = True
    plt.show()
    txt_de_cez = list(affine_decrypt(affine_encrypted_text, key))
    n_bin2_cez = len(set(txt_de_cez))
    s2 = plt.hist(txt_de_cez, bins=n_bin2_cez)

    plt.rcParams['patch.force_edgecolor'] = True
    plt.show()


    txt_en_viz = list(encode_vijn(b, c))
    n_bin1_viz = len(set(txt_en_viz))
    v1 = plt.hist(txt_en_viz, bins=n_bin1_viz)
    plt.rcParams['patch.force_edgecolor'] = True
    plt.show()
    txt_de_viz = list(decode_vijn(encode_viz, c))
    n_bin2_viz = len(set(txt_de_viz))
    v2 = plt.hist(txt_de_viz, bins=n_bin2_viz)

    plt.rcParams['patch.force_edgecolor'] = True
    plt.show()




ok_button1.bind('<Button-1>', main)
label_NAME_CEZ.grid(row=0, column = 1)
label1.grid(row=1, column=1)
entry1.grid(row=1, column=2)
label2.grid(row=3, column=1)
label2_1.grid(row=3, column=3)
Encrypt_output.grid(row=3, column=2)
label3.grid(row=4, column=1)
label3_1.grid(row=4, column=3)
Decrypted_output.grid(row=4, column=2)


label_NAME_VIZ.grid(row=5, column=1)
label_text_1.grid(row=6, column=1)
entry_text_1.grid(row=6, column=2)
label_text_2.grid(row = 7, column=1)
entry_text_2.grid(row=7, column=2)
en_text_1_viz.grid(row=6, column=3)
out_en_viz.grid(row=6, column=4)
time_viz_1.grid(row=6,column=5)
dec_text_1_viz.grid(row=7, column=3)
time_viz_2.grid(row=7, column= 5)
out_dec_viz.grid(row=7, column=4)


ok_button1.grid(row=10, column=1)
root.mainloop()
