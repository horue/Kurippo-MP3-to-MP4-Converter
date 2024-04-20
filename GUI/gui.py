import tkinter as tk
from tkinter import filedialog
import os 
import moviepy.editor as mp



def initial(root):
    t1 = tk.Label(root, text="MP3 to MP4 Converter")
    t1.pack()

    b1 = tk.Button(command=lambda:filedialog.askopenfile())
    b1.pack()



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