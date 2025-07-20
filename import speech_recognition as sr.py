import speech_recognition as sr

recognizer = sr.Recognizer()


with sr.Microphone() as source:
    print("🎤 Speak now...")
    recognizer.adjust_for_ambient_noise(source)  
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("✅ You said:", text)

        with open("transcription.txt", "w") as file:
            file.write(text)
            print("📝 Saved to 'transcription.txt'")

    except sr.UnknownValueError:
        print("❌ Could not understand your voice.")
    except sr.RequestError:
        print("🚫 Couldn't connect to the speech service.")
