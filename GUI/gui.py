import tkinter as tk
from tkinter import filedialog
import PIL
import os 
import moviepy.editor as mp


def run(b1, b2):
    outputPath = os.path.join(os.path.expanduser("~"), "Documents\\MP3 to MP4 Converter\\Converted Videos")
    if not os.path.exists(outputPath):
        os.makedirs(outputPath) 

    audio_path = b1.read
    image_path = b2.read
    audio = mp.AudioFileClip(audio_path, fps=44100)
    video = mp.VideoFileClip(image_path)


    video_duration = audio.duration


    final_video = video.set_audio(audio).set_duration(video_duration)


    final_video.write_videofile(outputPath, fps=60) 




    pass

def initial(root):
    t1 = tk.Label(root, text="MP3 to MP4 Converter")
    t1.pack()

    b1 = tk.Button(root, text='Select Image',command=lambda:filedialog.askopenfile())
    b1.pack()

    b2 = tk.Button(root, text='Select Sound',command=lambda:filedialog.askopenfile())
    b2.pack()

    b3 = tk.Button(root, text='Convert',command=lambda:run(b1, b2))
    b3.pack()



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