import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 200)    # Speed percent
engine.setProperty('volume', 1)  # Volume 0-1
engine.say("Hello, world!")
engine.runAndWait()