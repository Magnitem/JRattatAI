#Jarvis AI Voice Assistant in Russian
import speech_recognition as sr
import pyttsx3
import os
import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import webbrowser
import urllib.parse

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # скорость речи
    engine.setProperty('volume', 1.0)  # громкость
    # Выбираем голос (можно поэкспериментировать с индексом)
    voices = engine.getProperty('voices')
    if len(voices) > 0:
        engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    print("Скажите что-нибудь...")
    
    # Запись звука через sounddevice
    duration = 5  # секунд
    fs = 16000  # частота дискретизации
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    
    # Сохраняем в WAV файл
    wavfile.write("temp_audio.wav", fs, audio_data)
    
    try:
        with open("temp_audio.wav", "rb") as audio_file:
            audio = sr.AudioFile("temp_audio.wav")
            with audio as source:
                audio_data = r.record(source)
        
        query = r.recognize_google(audio_data, language='ru-RU')
        print(f"Вы сказали: {query}\n")
        os.remove("temp_audio.wav")
    except Exception as e:
        print("чё?")
        if os.path.exists("temp_audio.wav"):
            os.remove("temp_audio.wav")
        return "none"
    return query


def perform_search(query_text: str):
    """Open a Google search for the given text in the default browser."""
    if not query_text:
        return
    # Clean query: remove common trigger words
    triggers = ["найди", "поиск", "ищи", "что такое", "покажи"]
    cleaned = query_text
    for t in triggers:
        cleaned = cleaned.replace(t, "")
    cleaned = cleaned.strip()
    if not cleaned:
        speak("Что искать?")
        return
    speak(f"Ищу в Google: {cleaned}")
    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(cleaned)
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    speak("Привет! Я твой помощник. Чем могу помочь?")
    while True:
        query = listen().lower()
        if query == "none":
            continue

        # Время
        if any(phrase in query for phrase in ["сколько время", "который час"]):
            import datetime
            now = datetime.datetime.now()
            speak(f"Сейчас {now.hour} часов {now.minute} минут")
            continue
        if any(phrase in query for phrase in ["Powiedz cześć szymon", "Say hello szymon"]):
            speak("Fuck you Szymon")
            continue
        # Поисковые команды -> открыть браузер с Google
        if any(phrase in query for phrase in ["найди", "ищи", "поиск", "что такое", "покажи", "найти"]):
            perform_search(query)
            continue

        # Команды выхода
        if any(phrase in query for phrase in ["пока джарвисс", "пока", "выключи", "выход", "завершить", "закрыть", "до свидания", "всё, спасибо","Иди на фиг"]):
            speak("До свидания!")
            break

        speak("а?")