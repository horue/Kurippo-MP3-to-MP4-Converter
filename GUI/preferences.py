import customtkinter as ct
from customtkinter import filedialog
import sys
import os
from read_krip import *
from save_krip import *

    

class toplevel():

    def save(path, theme):
        save_path(p=path)
        save_theme(t=theme)
        
    def select_path(l1):
        global np
        np = filedialog.askdirectory()
        l1.configure(text=f'Conversion destiny: {np}')




    def preferences(title='Edit preferences', size='500x400'):
        tl = ct.CTkToplevel()
        tl.geometry(size)
        tl.title(title)
        tl.resizable(False, False)
        tl.grab_set()
        tl.iconbitmap(r'Visual\Kurippo_2.ico')

        l1 = ct.CTkLabel(tl, text=f'Conversion destiny: {get_path()}')
        l1.pack()

        b1 = ct.CTkButton(tl, text='Edit', command=lambda:toplevel.select_path(l1))
        b1.pack()

        
        l2 = ct.CTkLabel(tl, text=f'Theme: {get_theme()}')
        l2.pack()

        c1 = ct.CTkComboBox(tl, values=["Light", "Dark"])
        c1.pack()

        b3 = ct.CTkButton(tl, text='Save', command=lambda:toplevel.save(path=np, theme=c1.get()))
        b3.pack()

        b4 = ct.CTkButton(tl, text='Apply')
        b4.pack()


        for child in tl.winfo_children():
            child.pack_configure(padx=10, pady=15)


