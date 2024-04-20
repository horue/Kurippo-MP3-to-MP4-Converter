import tkinter as tk
from tkinter import filedialog
import PIL
import os 
import moviepy.editor as mp



def run():
    pass

def initial(root):
    t1 = tk.Label(root, text="MP3 to MP4 Converter")
    t1.pack()

    b1 = tk.Button(root, text='Select Image',command=lambda:filedialog.askopenfile())
    b1.pack()

    b2 = tk.Button(root, text='Select Sound',command=lambda:filedialog.askopenfile())
    b2.pack()

    b3 = tk.Button(root, text='Convert', command=lambda:run(b1, b2))
    b3.pack



def main():
    root = tk.Tk()
    root.title("MP3 to MP4 Converter")
    root.resizable(True, True)
                
    initial(root)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()


main()