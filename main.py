from tkinter import *
import time
from itertools import cycle
alp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
root = Tk()
root.title("Лабораторная работа №2")
root.geometry("450x200")
root.resizable(width=False, height=False)

value_textNEN = StringVar()
value_textEn = StringVar()
value_textDec = StringVar()

label_NAME_CEZ = Label(text="Шифр Цезаря")
label1 = Label(text="Ваш текст:")
entry1 = Entry(textvariable= value_textNEN)
ok_button1 = Button(text="Найти")
label2 = Label(text="Зашифрованный текст:")
label2_1 = Label(text="Время шифрования")
label3 = Label(text="Расшифрованный текст:")
label3_1 = Label(text="Время расшифрования")


label_NAME_VIZ = Label(text="Шифр Вижинера")


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
    a = value_textNEN.get()
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

    def encode_vijn(text, keytext):
        f = lambda arg: alp[(alp.index(arg[0]) + alp.index(arg[1]) % 33) % 33]
        return ''.join(map(f, zip(text, cycle(keytext))))

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
    vijin_encrypted_text = encode_vijn("ИЛЬЯ", "БУДНИК")
    print(vijin_encrypted_text)
    affine_encrypted_text = affine_encrypt(a, key)
    Encrypt_output['text'] = affine_encrypted_text
    Decrypted_output['text'] = affine_decrypt(affine_encrypted_text, key)
    #print(encode_vijn("Auto", "BUDNIK"))

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
ok_button1.grid(row=2, column=3)

label_NAME_VIZ.grid(row=5, column=1)


root.mainloop()
