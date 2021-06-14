from pyttsx3 import init

engine = init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',rate-100)

file = open('speech.txt')
speeches = file.read().split('\n')

for line in speeches:
	print(line)
	engine.say(line)
	engine.runAndWait()

file.close()