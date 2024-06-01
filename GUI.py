import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import font


class GUI:

    def vigenere_window(self):
        vigenere_window = tk.Toplevel()
        vigenere_window.title('VIGENERE CIPHER')
        vigenere_window.geometry("300x130")
        vigenere_window.resizable(False, False)
        vigenere_window.configure(bg='#1C1C1C')

        new_vigenere_table = ttk.Button(vigenere_window, text="New Vigenere Table")
        default_vigenere_table = ttk.Button(vigenere_window, text="Defualt Vigenere Table")
        decrypt_vigenere_cipher = ttk.Button(vigenere_window, text="Decrypt Vigenere Cipher")

        new_vigenere_table.pack(side="top", padx=5, pady=10)
        default_vigenere_table.pack(side="top", padx=5, pady=5)
        decrypt_vigenere_cipher.pack(side='top', padx=5, pady=5)



    def vigenere_window_2(self):
        vigenere_window_2 = tk.Toplevel()
        vigenere_window_2.title('VIGENERE CIPHER')
        #vigenere_window.geometry('300x300')

        dictionary_key_label = ttk.Label(vigenere_window_2, text='Dictionary-Key: ')
        key_stream_label = ttk.Label(vigenere_window_2, text='Key-Stream: ')

        dictionary_key = ttk.Entry(vigenere_window_2)
        key_stream = ttk.Entry(vigenere_window_2)

        dictionary_key_label.pack(side="top", padx=5, pady=5)
        dictionary_key.pack(side='top', padx=5, pady=5)
        key_stream_label.pack(side="top", padx=5, pady=5)
        key_stream.pack(side="top", padx=5, pady=5)

    def caesar_window(self):
        caesar_window = tk.Toplevel()
        caesar_window.title('CAESAR CIPHER')
        caesar_window.geometry('300X300')

    def gui(self):
        option_window = Tk()
        option_window.title('Cipher-Box')
        option_window.geometry('400x600')
        option_window.configure(bg='#1C1C1C')


        vigenere = ttk.Button(option_window, text="VIGENERE", command=self.vigenere_window)


        caesar = ttk.Button(option_window, text="CAESAR", command=self.caesar_window)


        vigenere.pack(side='top', expand=True, fill='both', pady=10, padx=80)
        caesar.pack(side='top', expand=True, fill='both', pady=10, padx=80)

        option_window.mainloop()


program = GUI()
program.gui()

