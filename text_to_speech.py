from gtts import gTTS

text = open("script.txt", encoding="utf-8").read()
tts = gTTS(text, lang="es")
tts.save("voice.mp3")
print("voice.mp3 oluşturuldu.")
