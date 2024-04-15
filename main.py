import moviepy.editor as mp
import easygui


def converter(nome, audioPath, imagePath):
    output_path = fr"c:\Users\jorge\Documents\{nome}.mp4"




    audio = mp.AudioFileClip(audioPath)



    video_duration = audio.duration

    video = mp.VideoClip(duration=video_duration)


    image_final = mp.ImageClip(imagePath)


    final_video = video.set_audio(audio).set_videoclip(image_final)


    final_video.write_videofile(output_path) 



audioPath = easygui.fileopenbox()
imagePath = easygui.fileopenbox()
nome = input('Qual o nome do vídeo?')
converter(nome, audioPath, imagePath)
