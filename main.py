import moviepy.editor as mp
import easygui


def converter(audioPath, imagePath):
    nome = easygui.enterbox('Qual o nome do vídeo? ')
    outputPath = fr"c:\Users\jorge\Documents\{nome}.mp4"


    audio = mp.AudioFileClip(audioPath, fps=44100)


    video_duration = audio.duration
    video = mp.VideoFileClip(audioPath).set_duration(video_duration)







    image_final = mp.ImageClip(imagePath).set_duration(video_duration)


    final_video = video.set_audio(audio).set_videoclip(image_final)


    final_video.write_videofile(outputPath, fps=30) 



audioPath = easygui.fileopenbox()
imagePath = easygui.fileopenbox()
converter(audioPath, imagePath)
