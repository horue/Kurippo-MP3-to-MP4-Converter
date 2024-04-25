import customtkinter as ct
import easygui as eg
import PIL
from PIL import Image
import os 
import moviepy.editor as mp
from CTkMessagebox import CTkMessagebox

def open_image():
    global image
    image = eg.fileopenbox()

def open_sound():
    global sound
    sound = eg.fileopenbox()


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
        CTkMessagebox(title='Aviso', message='Vídeo finalizado com sucesso!', icon='check')
    except:
        CTkMessagebox(title='Aviso', message='Nenhum arquivo foi selecionado.', icon='question')




def initial(root):
    t1 = ct.CTkLabel(root, text="MP3 to MP4 Converter")
    t1.pack(padx=15,pady=15)

    try:
        ph = ct.CTkImage(light_image=Image.open(image), dark_image=Image.open(image), size=(100, 100))
        i1 = ct.CTkLabel(root, text='', image=ph)
        i1.pack()
    except:
        path = 'ph.jpg'
        ph = ct.CTkImage(light_image=Image.open(path), dark_image=Image.open(path), size=(100, 100))
        i1 = ct.CTkLabel(root, text='', image=ph)
        i1.pack()

    b1 = ct.CTkButton(root, text='Select Image',command=open_image)
    b1.pack(padx=15,pady=5)

    b2 = ct.CTkButton(root, text='Select Sound',command=open_sound)
    b2.pack(padx=15,pady=5)

    b3 = ct.CTkButton(root, text='Convert',command=lambda:run())
    b3.pack(padx=15,pady=15)





def main():
    root = ct.CTk()
    root.geometry("400x250")
    root.title("MP3 to MP4 Converter")

    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()
main()