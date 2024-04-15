import moviepy.editor as mp


def converter(nome):
    audio_path = r"D:\Users\Eu\Music\MEmu Music\Teardrop.mp3"
    image = r"D:\Users\Eu\Music\MEmu Music\capabrz.png"
    output_path = fr"c:\Users\jorge\Documents\{nome}.mp4"




    audio = mp.AudioFileClip(audio_path)



    video_duration = audio.duration

    video = mp.VideoClip(duration=video_duration)


    image_final = mp.ImageClip(image)


    final_video = video.set_audio(audio).set_videoclip(image_final)


    final_video.write_videofile(output_path) 



nome = input('Qual o nome do vídeo?')
converter(nome)
