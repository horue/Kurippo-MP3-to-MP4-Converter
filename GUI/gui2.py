import customtkinter as ct
import easygui as eg
import PIL
from PIL import Image
import os 
import moviepy.editor as mp
from CustomTkinterMessagebox import CTkMessagebox

def open_image(i1, t3):
    global image
    image = eg.fileopenbox()
    ph = ct.CTkImage(light_image=Image.open(image), dark_image=Image.open(image), size=(100, 100))
    i1.configure(image=ph)
    t3.configure(text=image)

def open_sound(t5):
    global sound
    sound = eg.fileopenbox()
    t5.configure(text=sound)


def run():
    try:
        nome = str(os.path.basename(sound))
        name = os.path.splitext(nome)[0]

        outputPath = os.path.join(os.path.expanduser("~"), fr"Documents\{name}.mp4")

        audio = mp.AudioFileClip(str(sound), fps=44100)
        video = mp.VideoFileClip(str(image))


        video_duration = audio.duration


        final_video = video.set_audio(audio).set_duration(video_duration)


        final_video.write_videofile(outputPath, fps=60)
        CTkMessagebox.messagebox(title='Warning', text='Video converted successfully!')
        os.startfile(outputPath)
    except:
        CTkMessagebox.messagebox(title='Warning', text='Please select a sound and/or video\nbefore trying to convert.')




def initial(root):
    t1 = ct.CTkLabel(root, text="MP3 to MP4 Converter")
    t1.pack(padx=15,pady=15)

    t2 = ct.CTkLabel(root, text="Selected image: ")
    t3 = ct.CTkLabel(root, text="None")
    t2.pack(padx=15,pady=15)
    t3.pack()

    path = r'Visual\ph.jpg'
    ph = ct.CTkImage(light_image=Image.open(path), dark_image=Image.open(path), size=(100, 100))
    i1 = ct.CTkLabel(root, text='', image=ph)
    i1.pack(pady=15)

    t4=ct.CTkLabel(root, text="Selected audio: ")
    t5=ct.CTkLabel(root, text="None")
    t4.pack()
    t5.pack(pady=15)

    b1 = ct.CTkButton(root, text='Select Image',command=lambda:open_image(i1, t3))
    b1.pack(pady=5)

    b2 = ct.CTkButton(root, text='Select Audio',command=lambda:open_sound(t5))
    b2.pack(pady=5)

    b3 = ct.CTkButton(root, text='Convert',command=lambda:run())
    b3.pack(pady=15)

def options(root):
    tabview = ct.CTkTabview(master=root)
    tabview.pack(padx=20, pady=20)

    tabview.add("tab 1")  # add tab at the end
    tabview.add("tab 2")  # add tab at the end
    tabview.set("tab 2")  # set currently visible tab

    button = ct.CTkButton(master=tabview.tab("tab 1"))
    button.pack(padx=20, pady=20)



def main():
    root = ct.CTk()
    root.geometry("400x500")
    root.title("MP3 to MP4 Converter")

    
    options(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()