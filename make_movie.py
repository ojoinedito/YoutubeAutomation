from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

audio = AudioFileClip("voice.mp3")
duration = audio.duration / 3
clips = []
for i in range(1, 4):
    clip = VideoFileClip(f"videos/clip{i}.mp4").subclip(0, duration)
    clip = clip.resize((1080, 1920))
    clips.append(clip)
final = concatenate_videoclips(clips).set_audio(audio)
final.write_videofile("output.mp4", fps=24, codec="libx264")
print("output.mp4 oluşturuldu.")
