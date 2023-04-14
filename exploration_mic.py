"""
Final
===========================
Student:  Jessica Hwang
Semester: Spring 2023

Exploration for final project - microphone focused
"""
import speech_recognition as sr
r = sr.Recognizer()

mic = sr.Microphone()

print(sr.Microphone.list_microphone_names())


with mic as source:
    print("speak:")
    audio = r.listen(source)

try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))