import speech_recognition as sr

record = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything... -> ")

    audio = record.listen(source)
    # try:
    #     text = record.recognize_bing(audio)

    #     print(f'Google think u said :-> {text}')

    # except:
    #     print('sorry')

    text = record.recognize_google(audio)

    print(f'Google think u said :-> {text}')
