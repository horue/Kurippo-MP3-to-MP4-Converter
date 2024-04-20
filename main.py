import moviepy.editor as mp
import easygui
import os


def converter(audioPath, imagePath):
    nome = str(os.path.basename(audioPath))
    outputPath = os.path.join(os.path.expanduser("~"), "Documents\\MP3 to MP4 Converter\\Converted Videos")
    if not os.path.exists(outputPath):
        os.makedirs(outputPath) 



    audio = mp.AudioFileClip(audioPath, fps=44100)
    video = mp.VideoFileClip(imagePath)


    video_duration = audio.duration


    final_video = video.set_audio(audio).set_duration(video_duration)


    final_video.write_videofile(outputPath, fps=60) 



audioPath = easygui.fileopenbox()
imagePath = easygui.fileopenbox()
converter(audioPath, imagePath)
