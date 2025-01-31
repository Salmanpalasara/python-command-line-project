import pyttsx3 as tx

hello = tx.init()


voices = hello.getProperty('voices')
hello.setProperty('voices', voices[1].id)

text = input("Enter a text here...")

hello.say(text)

hello.runAndWait()
hello.stop()