import tkinter as tk
import tkinter as ttk

class VigenereApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Vigenere")
        #self.geometry('300x130')
        #self.resizable(False, False)

        #widgets
        #MainMenu(self)
        NewVigenereTable(self)
        self.mainloop()


    def switch_frames(self):
        pass


class MainMenu(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.geometry('300x130')

        #ttk.Label(self, background = 'red').pack(expand = True, fill = 'both')

        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.create_widget()

    def create_widget(self):
        # create grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Create and place the label
        label1 = ttk.Label(self, text="Label 1", background='blue')
        label1.grid(row=0, column=0, sticky='nsew')

        # If you want to add more labels and make them span the entire column width, add them here.
        # For example, to create labels for row 1 and row 2:
        label2 = ttk.Label(self, text="Label 2", background='green')
        label2.grid(row=1, column=0, sticky='nsew')

        label3 = ttk.Label(self, text="Label 3", background='red')
        label3.grid(row=2, column=0, sticky='nsew')

        new_vigenere_table_button = ttk.Button(self, text = 'New Vigenere Table').grid(row = 0, column = 0)
        default_vigenere_table_button = ttk.Button(self, text = 'Default Vigenere Table').grid(row = 1, column = 0)
        decrypt_vigenere_cipher_button = ttk.Button(self, text = 'Decrypt Vigenere Cipher').grid(row = 2, column = 0)


class NewVigenereTable(ttk.Frame):

    """
               Entry: Dictionary_Key
            Entry: Key Stream

            Label: 'Text'
            Entry: text

            Button: Encrypt


    """
    def __init__(self, parent):
        super().__init__(parent)
        # parent.geometry('350x400')

        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        # create grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        # Create and place the label
        label1 = ttk.Label(self, text="Label 1", background='blue')
        label1.grid(row=0, column=0, sticky='nsew', columnspan = 2)

        # If you want to add more labels and make them span the entire column width, add them here.
        # For example, to create labels for row 1 and row 2:


        label4 = ttk.Label(self, text = "Label 4", background = 'orange')
        label4.grid(row = 3, column = 0, sticky = 'nsew')

        label5 = ttk.Label(self, text="Label 5", background='brown')
        label5.grid(row=4, column=0, sticky='nsew')

        dictionary_key_label = ttk.Label(self, text='Dictionary Key')
        dictionary_key_label.grid(row=1, column=0, sticky='n', pady=(30, 0))
        dictionary_key_entry = ttk.Entry(self, width = 10, background = 'white')
        dictionary_key_entry.grid(row = 1, column = 0, sticky = 's', pady=(0, 20))

        key_stream = ttk.Label(self, text = 'Key Stream').grid(row = 2, column = 0, sticky = 'n', pady=(30, 0))
        key_stream_entry = ttk.Entry(self, width = 10, background = 'white')
        key_stream_entry.grid(row = 2, column = 0, sticky = 's', pady = (0,19))

        text_box = ttk.Text(self, width = 10, height = 5, background = 'white')
        text_box.grid(row = 3, column = 0, sticky = 'ew', columnspan = 2, padx=10, pady=10)



