import moviepy.editor as mp
import easygui
import os

image_types = ['*.jpg', '*.jpeg']
audio_types = ['*.mp3']


def converter(audioPath, imagePath):
    nome = str(os.path.basename(audioPath))
    name = os.path.splitext(nome)[0]

    outputPath = os.path.join(os.path.expanduser("~"), fr"Documents\{name}.mp4")

    audio = mp.AudioFileClip(audioPath, fps=44100)
    video = mp.VideoFileClip(imagePath)


    video_duration = audio.duration


    final_video = video.set_audio(audio).set_duration(video_duration)


    final_video.write_videofile(outputPath, fps=60) 



audioPath = easygui.fileopenbox(msg="Select Audio",title='Audio', default='*.mp3', filetypes=audio_types)
imagePath = easygui.fileopenbox(msg="Select Image",title='Image', default='*.jpg', filetypes=image_types)
converter(audioPath, imagePath)
