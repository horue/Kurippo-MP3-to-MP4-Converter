import tkinter as tk
import easygui as eg
import PIL
import os 
import moviepy.editor as mp




def open_image():
    global image
    image = eg.fileopenbox()

def open_sound():
    global sound
    sound = eg.fileopenbox()


def run():
    nome = str(os.path.basename(sound))
    name = os.path.splitext(nome)[0]

    outputPath = os.path.join(os.path.expanduser("~"), fr"Documents\{name}.mp4")

    audio = mp.AudioFileClip(str(sound), fps=44100)
    video = mp.VideoFileClip(str(image))


    video_duration = audio.duration


    final_video = video.set_audio(audio).set_duration(video_duration)


    final_video.write_videofile(outputPath, fps=60) 


def initial(root):
    t1 = tk.Label(root, text="MP3 to MP4 Converter")
    t1.pack()

    b1 = tk.Button(root, text='Select Image',command=open_image)
    b1.pack()

    b2 = tk.Button(root, text='Select Sound',command=open_sound)
    b2.pack()

    b3 = tk.Button(root, text='Convert',command=lambda:run())
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