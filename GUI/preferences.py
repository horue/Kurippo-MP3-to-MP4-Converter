import customtkinter as ct
import sys
import os
from read_krip import *


class toplevel():
    def preferences(title='Edit preferences', size='500x400'):
        tl = ct.CTkToplevel()
        tl.geometry(size)
        tl.title(title)
        tl.resizable(False, False)
        tl.grab_set()
        tl.iconbitmap(r'Visual\Kurippo_2.ico')

        l1 = ct.CTkLabel(tl, text=f'Conversion destiny: {get_path()}')
        l1.pack()

        b1 = ct.CTkButton(tl, text='Edit')
        b1.pack()

        
        l2 = ct.CTkLabel(tl, text=f'Theme: {get_theme()}')
        l2.pack()

        b2 = ct.CTkButton(tl, text='Edit')
        b2.pack()

        b3 = ct.CTkButton(tl, text='Save')
        b3.pack()


        for child in tl.winfo_children():
            child.pack_configure(padx=10, pady=15)


