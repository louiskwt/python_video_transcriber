import speech_recognition as sr
import moviepy.editor as mp

# Extracing the audio from a video in the same directory
clip = mp.VideoFileClip(r"animals.mp4")
clip.audio.write_audiofile(r"converted.wav")

# Defining the recognizer and importing the audio file
r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")

# Recognizing the audio using Google Speech Recognization
with audio as source:
    r.adjust_for_ambient_noise(source)
    audio_file = r.record(source)

result = r.recognize_google(audio_file)


# Exporting the result
with open('script.txt', mode='w') as file:
    file.write("Recongized Speech: ")
    file.write("\n")
    file.write("\n")
    file.write(result)
    print("The script is ready!")

file.close()
