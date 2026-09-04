import pyttsx3

# Create the speech engine
engine = pyttsx3.init()

# Text to speak
engine.say("Hello Ankur, welcome to Python!")

# Speak the text
engine.runAndWait()