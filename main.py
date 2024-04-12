import moviepy.editor as mp



audio_path = r"D:\Users\Eu\Music\MEmu Music\Teardrop.mp3"

audio = mp.AudioFileClip(audio_path)

image = r"D:\Users\Eu\Music\MEmu Music\capabrz.png"


video_duration = audio.duration
video = mp.VideoClip(duration=video_duration)
video.duration = video_duration


image_final = mp.ImageClip(image) .set_duration(video_duration)


final_video = video.set_audio(audio).set_videoclip(image_final)


output_path = r"D:\Users\Eu\Music\MEmu Music\ga.mp4"
final_video.write_videofile(output_path) 